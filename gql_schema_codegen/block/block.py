import os
import re
from typing import Dict, List, Literal, NamedTuple, Optional, Set, Union

from ..base import BaseInfo
from ..constants import RESOLVER_TYPES, VALUE_TYPES
from ..constants.block_fields import all_block_fields
from ..dependency import (Dependency, DependencyGroup,
                          get_interface_dependencies,
                          remove_interface_dependencies)
from ..utils import pascal_case


class BlockFieldInfo(NamedTuple):
    name: str
    parent_type: str
    parent_name: str
    params: Optional[str]
    is_field_from_params: Optional[bool]
    value_type: str


# a dictionary where for each node, we hold its children
inheritanceTree: Dict[str, Set[str]] = {"root": set()}


def get_inheritance_tree():
    return inheritanceTree


class Block(BaseInfo):
    def __init__(self, info, dependency_group: DependencyGroup) -> None:
        super().__init__(info)
        self.dependency_group = dependency_group
        self.parent_classes = set()

    @property
    def display_name(self):
        display_name = pascal_case(self.name)

        if self.type == "param_type":
            display_name = f"{display_name}Params"

        return display_name

    @property
    def heading_file_line(self):
        global inheritanceTree
        display_name = self.display_name

        if self.type == "enum":
            self.dependency_group.add_dependency(
                Dependency(imported_from="enum", dependency="Enum")
            )
            return f"class {display_name}(str, Enum):"

        self.dependency_group.add_dependency(
            Dependency(imported_from="dataclasses", dependency="dataclass")
        )
        self.dependency_group.add_dependency(
            Dependency(imported_from="dataclasses", dependency="field")
        )
        self.dependency_group.add_dependency(
            Dependency(
                imported_from="mashumaro.mixins.json", dependency="DataClassJSONMixin"
            )
        )
        self.dependency_group.add_dependency(
            Dependency(imported_from="mashumaro.config", dependency="BaseConfig")
        )

        if not self.implements:
            # check if we have an interface implementing another interface
            deps = get_interface_dependencies()
            if display_name in deps:
                siblings = inheritanceTree.get(deps[display_name], set())
                siblings.add(display_name)
                inheritanceTree[deps[display_name]] = siblings
                return f"@dataclass(kw_only=True)\nclass {display_name}({deps[display_name]}):"

            inheritanceTree["root"].add(display_name)
            return (
                f"@dataclass(kw_only=True)\nclass {display_name}(DataClassJSONMixin):"
            )

        parents = remove_interface_dependencies(
            [x.strip() for x in self.info.implements.split("&")]  # type: ignore
        )
        for p in parents:
            siblings = inheritanceTree.get(p, set())
            siblings.add(display_name)
            inheritanceTree[p] = siblings
        parent_str = ", ".join(parents)
        return f"@dataclass(kw_only=True)\nclass {display_name}({parent_str}):"

    @property
    def category(self):
        if self.type == "enum":
            return "enum"

        if self.type == "scalar":
            return "scalar"

        if self.type == "param_type":
            return "param_type"

        return None

    @property
    def file_representation(self):
        lines_with_deps: List[str] = []
        lines: List[str] = []

        if self.type == "enum":
            lines.append(self.heading_file_line)
            for x in map(lambda f: f.name, self.fields):
                lines.append(f'    {x} = "{x}"')
            return "\n".join(lines)

        if self.heading_file_line is not None:
            lines.append(self.heading_file_line)

        parent_fields = set()
        for p in self.parent_classes:
            parent_fields.update(all_block_fields.get(p, set()))
        for f in self.fields:
            # don't re-include parent fields
            if str(f).split(":")[1].strip() in parent_fields:
                continue

            if "dateutil.parser" in str(f.file_line) and "default=None" in str(
                f.file_line
            ):
                lines_with_deps.append(f"    {f.file_line}")
            elif "Optional[" in str(f.file_line):
                if "dateutil.parser.isopare" in str(f.file_line):
                    lines_with_deps.append(
                        '    Optional[datetime] = field(default=None, metadata={"deserialize": lambda d: d.to_native() if isinstance(d, neo4j.time.DateTime) else dateutil.parser.isoparse(d), "serialize": lambda v: v.isoformat()})'
                    )
                else:
                    lines_with_deps.append(f"    {f.file_line} = field(default=None)")
            else:
                lines.append(f"    {f.file_line}")

        suffix = [
            "",
            " " * 4 + "class Config(BaseConfig):",
            " " * 8 + 'code_generation_options = ["TO_DICT_ADD_OMIT_NONE_FLAG"]',
        ]
        return "\n".join(lines + lines_with_deps + suffix)

    def __repr__(self):
        return f"Block: {self.type} {self.name} ({len(self.fields)} fields)"


class BlockField(BaseInfo):

    _param_blocks: List[Block] = []

    def __init__(self, info: BlockFieldInfo, dependency_group: DependencyGroup) -> None:
        super().__init__(info)
        self.dependency_group = dependency_group

    def value_type_str(self, v_type: Optional[str] = None):
        val_type = self.value_type if not v_type else v_type

        # remove params from value type
        val_type = re.sub(r"\s=\s.+", "", val_type)

        if val_type is None:
            return None

        if val_type.endswith("!"):
            val_type = val_type[:-1]

        is_array = val_type.startswith("[") and val_type.endswith("]")
        is_array_item_required = False

        cleaned_value_type = val_type
        if is_array:
            is_array_item_required = val_type.endswith("!]")
            cleaned_value_type = val_type[1:-1]

            if is_array_item_required:
                cleaned_value_type = cleaned_value_type[:-1]
            else:
                self.dependency_group.add_dependency(
                    Dependency(imported_from="typing", dependency="Optional")
                )

            self.dependency_group.add_dependency(
                Dependency(imported_from="typing", dependency="List")
            )
            return f"List[{self.value_type_str(cleaned_value_type)}]"

        item_type = VALUE_TYPES.get(cleaned_value_type, f"{cleaned_value_type}")

        if is_array and not is_array_item_required:
            if "dateutil.parser.isoparse" in str(item_type):
                item_type = 'Optional[datetime] = field(default=None, metadata={"deserialize": lambda d: d.to_native() if isinstance(d, neo4j.time.DateTime) else dateutil.parser.isoparse(d), "serialize": lambda v: v.isoformat()})'
            else:
                item_type = f'Optional["{item_type}"]'

        return item_type if not is_array else f'List["{item_type}"]'

    @property
    def required(self):
        return self.value_type is not None and self.value_type.endswith("!")

    @property
    def type_str(self):
        if self.parent_type == "enum":
            return f'"{self.name}"'

        v_type_str = self.value_type_str()
        if v_type_str is not None and v_type_str not in list(VALUE_TYPES.values()):
            v_type_str = pascal_case(v_type_str)

        if not self.required:
            self.dependency_group.add_dependency(
                Dependency(imported_from="typing", dependency="Optional")
            )
            if "dateutil.parser.isoparse" in str(v_type_str):
                return 'Optional[datetime] = field(default=None, metadata={"deserialize": lambda d: d.to_native() if isinstance(d, neo4j.time.DateTime) else dateutil.parser.isoparse(d), "serialize": lambda v: v.isoformat()})'
            else:
                return f"Optional[{v_type_str}]"

        return v_type_str

    @property
    def is_possible_resolver_type(self):
        return self.parent_name in RESOLVER_TYPES

    @property
    def result_definition_name(self):
        if self.is_possible_resolver_type and not self.is_field_from_params:
            return f"{pascal_case(self.name)}{self.parent_name}Result"

    @property
    def result_definition(self):
        if self.result_definition_name:
            v_type_str = self.value_type_str()
            if v_type_str not in list(VALUE_TYPES.values()):
                self.dependency_group.add_dependency(
                    Dependency(imported_from="typing", dependency="TypeAlias")
                )
                return f'{self.result_definition_name}: TypeAlias = "{v_type_str}"'

            return f"{self.result_definition_name} = {v_type_str}"

    @property
    def file_line(self):
        if self.result_definition_name:
            return f'{self.name}: "{self.result_definition_name}"'

        if self.parent_type == "enum":
            return f'{self.name} = "{self.type_str}"'

        if "dateutil" in str(self.type_str):
            return f"{self.name}: {self.type_str}"
        return f'{self.name}: "{self.type_str}"'

    @property
    def param_block(self):
        if self.params is None:
            return None

        fields: List[BlockField] = []

        for param in re.split(",|\n", self.params):
            if param.strip() == "":
                continue

            param_name, param_type = param.strip().replace(": ", ":").split(":")
            info = BlockFieldInfo(
                name=param_name,
                parent_type=self.parent_type,
                parent_name=self.parent_name,
                params=None,
                is_field_from_params=True,
                value_type=param_type,
            )
            f = BlockField(info, dependency_group=self.dependency_group)
            fields.append(f)

        block_info = BlockInfo(
            type="param_type",
            name=self.name,
            fields=fields,
            implements=None,
        )
        b = Block(block_info, dependency_group=self.dependency_group)

        return b

    def __repr__(self):
        return f"Field: {self.name}"


class BlockInfo(NamedTuple):
    type: Union[
        Literal["param_type"], Literal["type"], Literal["input"], Literal["enum"]
    ]
    name: str
    implements: Optional[str]
    fields: List[BlockField]
