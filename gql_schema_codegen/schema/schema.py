import json
import os
import re
import subprocess
from typing import Dict, List, Optional, Set

import yaml
from graphql import (
    build_client_schema,
    build_schema,
    get_introspection_query,
    print_schema,
)
from graphqlclient import GraphQLClient

from ..block import (
    Block,
    BlockField,
    BlockFieldInfo,
    BlockInfo,
    get_inheritance_tree,
)
from ..constants import (
    BLOCK_PATTERN,
    DIRECTIVE_PATTERN,
    DIRECTIVE_USAGE_PATTERN,
    FIELD_PATTERN,
    RESOLVER_TYPES,
    SCALAR_PATTERN,
    UNION_PATTERN,
)
from ..constants.block_fields import all_block_fields
from ..dependency import (
    Dependency,
    DependencyGroup,
    update_interface_dependencies,
)
from ..scalar import ScalarInfo, ScalarType
from ..union import UnionInfo, UnionType


class Schema:
    _string: Optional[str] = None
    _blocks: List[Block] = []
    _cleaned_string: Optional[str] = None
    _unions: List[UnionType] = []
    _scalars: List[ScalarType] = []
    ignore_types: List[str] = []
    generate_empty_params_types = False
    path: Optional[str] = None
    url: Optional[str] = None
    _config_file_content = None
    config_file: Optional[str] = None
    _special_blocks: Set[str] = set()
    _import_blocks: Optional[str] = None
    _only_blocks: bool = False

    def __init__(self, **kwargs) -> None:
        if "path" in kwargs and isinstance(kwargs["path"], str):
            self.path = kwargs["path"]

        if "url" in kwargs and isinstance(kwargs["url"], str):
            self.url = kwargs["url"]

        if "config_file" in kwargs and isinstance(kwargs["config_file"], str):
            self.config_file = kwargs["config_file"]

        self._special_blocks = kwargs.get("blocks", self._special_blocks)
        self._import_blocks = kwargs.get("import_blocks", self._import_blocks)
        self._only_blocks = kwargs.get("only_blocks", self._only_blocks)

        update_interface_dependencies(self.config_file_content)

        # FIXME dependencies are not properly pulled in cases of --only flags
        # etc
        self.dependency_group = DependencyGroup()
        self.dependency_group.add_dependency(
            Dependency(imported_from="dataclasses", dependency="dataclass")
        )
        self.dependency_group.add_dependency(
            Dependency(imported_from="dataclasses", dependency="field")
        )
        self.dependency_group.add_dependency(
            Dependency(imported_from="datetime", dependency="datetime")
        )
        self.dependency_group.add_direct_dependency("dateutil.parser")

    @property
    def config_file_content(self) -> Optional[dict[str, str]]:
        if (
            self._config_file_content is None
            and self.config_file
            and os.path.exists(self.config_file)
        ):
            with open(self.config_file, "r") as f:
                return yaml.safe_load(f)

        return self._config_file_content

    @property
    def custom_scalars(self) -> dict[str, str]:
        if isinstance(self.config_file_content, dict):
            data = self.config_file_content.get("scalars")
            if isinstance(data, dict):
                return data

        return {}

    def generate_type_file(self, to_path: str):
        with open(f"{to_path}", "w") as f:
            f.write(self.file_representation)
            return self.file_representation

    def get_sdl(self):
        if self.url:
            client = GraphQLClient(self.url)
            query_intros = get_introspection_query(descriptions=False)
            intros_result = client.execute(query_intros, variables=None)
            intros = json.loads(intros_result)
            client_schema = build_client_schema(intros.get("data", None))
            sdl = print_schema(client_schema)
            return sdl

        return None

    @property
    def is_schema_path(self):
        return bool(self.path and os.path.isdir(self.path))

    def read_schema(self):
        if self.path:
            with open(self.path, "r") as f:
                return f.read()

        if self.url:
            return self.get_sdl()

        return None

    @property
    def string(self):
        if not self._string:
            self._string = self.read_schema()

        return self._string

    # FIXME add support for directives
    @staticmethod
    def clean_string(string: str):
        cleaned = re.sub(r"\s+#.+\n", "\n", string)

        cleaned = re.sub(r'\n?"{3}[^"]+"{3}\n?', "", cleaned)

        # remove empty lines
        cleaned = re.sub(r"[\s\t]+\n", "\n", cleaned, flags=re.MULTILINE)

        # remove lines with directives
        cleaned = re.sub(DIRECTIVE_PATTERN, "", cleaned)

        cleaned = re.sub(DIRECTIVE_USAGE_PATTERN, "", cleaned)

        cleaned = re.sub(r"\s=\s\{\}", "", cleaned)
        return cleaned

    @property
    def cleaned_string(self):
        if not self._cleaned_string:
            if self.string:
                self._cleaned_string = Schema.clean_string(self.string)
            else:
                self._cleaned_string = ""

        return self._cleaned_string

    @staticmethod
    def get_fields_from_block(fields: str):
        return map(
            lambda it: it.groupdict(),
            re.finditer(FIELD_PATTERN, Schema.clean_string(fields)),
        )

    def get_blocks(self):
        return map(
            lambda it: it.groupdict(),
            re.finditer(BLOCK_PATTERN, self.cleaned_string, re.MULTILINE),
        )

    def get_unions(self):
        return map(
            lambda it: it.groupdict(),
            re.finditer(UNION_PATTERN, self.cleaned_string, re.MULTILINE),
        )

    def get_scalars(self):
        return map(
            lambda it: it.groupdict(),
            re.finditer(SCALAR_PATTERN, self.cleaned_string, re.MULTILINE),
        )

    @property
    def blocks(self):
        if not self._blocks:
            blocks: List[Block] = []
            _blocks = list(self.get_blocks())

            for block in _blocks:
                block_fields: List[BlockField] = []

                block_type = block["type"]
                block_name = block["name"]
                all_block_fields[block_name] = set()
                for field in self.get_fields_from_block(block["fields"]):
                    all_block_fields[block_name].add(field["name"])

                    info = BlockFieldInfo(
                        name=field["name"],
                        parent_type=block_type,
                        parent_name=block_name,
                        params=field["params"],
                        is_field_from_params=False,
                        value_type=field["value_type"],
                    )
                    f = BlockField(info, dependency_group=self.dependency_group)
                    block_fields.append(f)

                block_info = BlockInfo(
                    type=block_type,
                    name=block["name"],
                    fields=block_fields,
                    implements=block["implements"],
                )
                b = Block(block_info, dependency_group=self.dependency_group)

                if self._import_blocks and block_type in self._special_blocks:
                    self.dependency_group.add_dependency(
                        Dependency(self._import_blocks, b.display_name)
                    )
                elif self._only_blocks and block_type not in self._special_blocks:
                    continue
                else:
                    blocks.append(b)

            self._blocks = list(
                filter(lambda b: b.name not in self.ignore_types, blocks)
            )

        return self._blocks

    @property
    def sorted_blocks(self):
        # first populate inheritance tree. this is VERY dirty for now but we
        # should refactor this soon. We are calling b.heading_file_line for all
        # blocks here as this is what populates the tree, and we only do this
        # once
        all_blocks: Dict[str, Block] = {}
        for b in self.blocks:
            all_blocks[b.name] = b
            _ = b.heading_file_line
        inheritanceTree = get_inheritance_tree()
        sorted_bl: List[Block] = []
        # first add enums - these have no dependencies
        sorted_bl.extend(list(filter(lambda x: x.type == "enum", self.blocks)))

        types_order = ["interface", "type", "param_type", "input"]
        for t in types_order:
            interfaces = list(filter(lambda x: x.type == t, self.blocks))

            to_add = {b.name for b in interfaces}
            blocks: List[Block] = []

            # add nodes in a BFS manner to ensure we don't break dependencies
            queue: List[str] = ["root"]
            visited: Set[str] = set(["root"])
            while queue:
                node = queue.pop(0)
                if node in to_add:
                    blocks.append(all_blocks[node])
                for child_node in inheritanceTree.get(node, []):
                    if child_node not in visited:
                        visited.add(child_node)
                        queue.append(child_node)

            sorted_bl.extend(blocks)
        sorted_bl.sort(key=lambda x: x.display_name)
        return sorted_bl

    @property
    def unions(self):
        if not self._unions:
            self._unions = []

            for u in self.get_unions():
                union_info = UnionInfo(name=u["name"], types=u["types"])
                self._unions.append(
                    UnionType(union_info, dependency_group=self.dependency_group)
                )

        return self._unions

    @property
    def scalars(self):
        if not self._scalars:
            self._scalars = []

            for u in self.get_scalars():
                scalar_info = ScalarInfo(
                    name=u["name"], value=self.custom_scalars.get(u["name"])
                )
                scalar = ScalarType(scalar_info, dependency_group=self.dependency_group)
                if self._import_blocks and "scalar" in self._special_blocks:
                    # hack to adjust dependency group
                    scalar.file_representation
                    self.dependency_group.add_dependency(
                        Dependency(self._import_blocks, scalar_info.name)
                    )
                else:
                    self._scalars.append(scalar)

        if self._only_blocks and "scalar" not in self._special_blocks:
            return []

        return self._scalars

    @property
    def import_lines(self):
        return self.dependency_group.import_lines

    @property
    def file_representation(self):
        lines: List[str] = ["\n" * 2]

        if len(self.scalars) > 0:
            for s in self.scalars:
                lines.extend([s.file_representation] + ["\n"])

        lines.append("\n" * 2)

        if len(self.unions) > 0:
            self.dependency_group.add_dependency(
                Dependency(imported_from="typing", dependency="Union")
            )
            for u in self.unions:
                lines.extend([u.file_representation] + ["\n" * 2])

        for b in self.sorted_blocks:
            lines.extend([b.file_representation] + ["\n" * 3])

            if b.name in RESOLVER_TYPES:
                for f in b.fields:
                    field: BlockField = f
                    if field.param_block and (
                        len(field.param_block.fields) > 0
                        or self.generate_empty_params_types
                    ):
                        lines.extend([field.param_block.file_representation, "\n" * 3])

                    if field.result_definition:
                        lines.extend([field.result_definition, "\n" * 3])

        lines.insert(0, self.import_lines)

        return "".join(lines)
