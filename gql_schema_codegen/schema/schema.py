import json
import re
import os
import subprocess
from graphql import get_introspection_query, print_schema, build_client_schema, build_schema
from graphqlclient import GraphQLClient
from typing import List, Optional
import yaml
from ..scalar import ScalarInfo, ScalarType
from ..block import Block, BlockInfo, BlockField, BlockFieldInfo
from ..dependency import Dependency, DependencyGroup
from ..constants import DIRECTIVE_PATTERN, DIRECTIVE_USAGE_PATTERN, SCALAR_PATTERN, UNION_PATTERN, BLOCK_PATTERN, FIELD_PATTERN, RESOLVER_TYPES
from ..union import UnionType, UnionInfo


class Schema:

    _string: Optional[str] = None
    _blocks: List[Block] = []
    _cleaned_string: Optional[str] = None
    _unions: List[UnionType] = []
    _scalars: List[ScalarType] = []
    ignore_types = []
    generate_empty_params_types = False
    path: Optional[str] = None
    url: Optional[str] = None
    _config_file_content = None
    config_file: Optional[str] = None

    def __init__(self, **kwargs) -> None:
        if 'path' in kwargs and type(kwargs['path']) is str:
            self.path = kwargs['path']

        if 'url' in kwargs and type(kwargs['url']) is str:
            self.url = kwargs['url']

        if 'config_file' in kwargs and type(kwargs['config_file']) is str:
            self.config_file = kwargs['config_file']

        self.dependency_group = DependencyGroup()

    @property
    def config_file_content(self) -> Optional[dict[str, str]]:
        if self._config_file_content is None and self.config_file and os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return yaml.safe_load(f)

        return self._config_file_content

    @property
    def custom_scalars(self) -> dict[str, str]:
        if type(self.config_file_content) is dict:
            data = self.config_file_content.get('scalars')
            if type(data) is dict:
                return data

        return {}

    def generate_type_file(self, to_path: str):
        with open(f"{to_path}", 'w') as f:
            f.write(self.file_representation)
            return self.file_representation

    def get_sdl(self):
        if self.url:
            client = GraphQLClient(self.url)
            query_intros = get_introspection_query(descriptions=False)
            intros_result = client.execute(
                query_intros, variables=None)
            intros = json.loads(intros_result)
            client_schema = build_client_schema(
                intros.get('data', None))
            sdl = print_schema(client_schema)
            return sdl

        return None

    @property
    def is_schema_path(self):
        return bool(self.path and os.path.isdir(self.path))

    @property
    def marged_schema_from_dir(self):
        INSTALLATION_COMMAND = 'npm list -g graphql-schema-utilities ||npm i --global graphql-schema-utilities'
        if self.is_schema_path and self.path:
            try:
                subprocess.call(INSTALLATION_COMMAND, shell=True,
                                stdout=subprocess.DEVNULL)
            except:
                pass

            glob_paths = [os.path.join(
                self.path, '**/*.gql'), os.path.join(self.path, '**/*.graphql')]
            joined_glob_paths = ','.join(glob_paths)
            MERGE_COMMAND = f'graphql-schema-utilities -s "{{{joined_glob_paths}}}"'
            output = subprocess.run(
                MERGE_COMMAND, shell=True, text=True, capture_output=True)
            return output.stdout

    def read_schema(self):
        if self.is_schema_path:
            return self.marged_schema_from_dir

        if self.path:
            with open(self.path, 'r') as f:
                return f.read()

        if self.url:
            return self.get_sdl()

        return None

    @property
    def string(self):
        if not self._string:
            self._string = self.read_schema()

        return self._string

    @staticmethod
    def clean_string(string: str):
        cleaned = re.sub(r'\s+#.+\n', '\n', string)

        cleaned = re.sub(r'\n?"{3}[^"]+"{3}\n?', '', cleaned)

        # remove empty lines
        cleaned = re.sub(r'[\s\t]+\n', '\n', cleaned, flags=re.MULTILINE)

        # remove lines with directives
        cleaned = re.sub(DIRECTIVE_PATTERN, '', cleaned)

        cleaned = re.sub(DIRECTIVE_USAGE_PATTERN, '', cleaned)

        cleaned = re.sub(r'\s=\s\{\}', '', cleaned)
        return cleaned

    @property
    def cleaned_string(self):
        if not self._cleaned_string:
            if self.string:
                self._cleaned_string = Schema.clean_string(self.string)
            else:
                self._cleaned_string = ''

        return self._cleaned_string

    @staticmethod
    def get_fields_from_block(fields: str):
        return map(lambda it: it.groupdict(), re.finditer(FIELD_PATTERN, Schema.clean_string(fields)))

    def get_blocks(self):
        return map(lambda it: it.groupdict(), re.finditer(BLOCK_PATTERN, self.cleaned_string, re.MULTILINE))

    def get_unions(self):
        return map(lambda it: it.groupdict(), re.finditer(UNION_PATTERN, self.cleaned_string, re.MULTILINE))

    def get_scalars(self):
        return map(lambda it: it.groupdict(), re.finditer(SCALAR_PATTERN, self.cleaned_string, re.MULTILINE))

    @property
    def blocks(self):
        if not self._blocks:
            blocks: List[Block] = []
            _blocks = list(self.get_blocks())

            for block in _blocks:
                block_fields: List[BlockField] = []

                block_type = block['type']
                block_name = block['name']

                for field in self.get_fields_from_block(block['fields']):
                    info = BlockFieldInfo(name=field['name'],
                                          parent_type=block_type,
                                          parent_name=block_name,
                                          params=field['params'],
                                          is_field_from_params=False,
                                          value_type=field['value_type'])
                    f = BlockField(
                        info, dependency_group=self.dependency_group)
                    block_fields.append(f)

                block_info = BlockInfo(
                    type=block_type, name=block['name'], fields=block_fields, implements=block['implements'])
                b = Block(block_info, dependency_group=self.dependency_group)

                blocks.append(b)

            self._blocks = list(
                filter(lambda b: b.name not in self.ignore_types, blocks))

        return self._blocks

    @property
    def sorted_blocks(self):
        types_order = ['enum', 'type', 'param_type', 'input']
        return sorted(self.blocks, key=lambda b: (types_order.index(
            b.type) if b.type in types_order else -1))

    @property
    def unions(self):
        if not self._unions:
            self._unions = []

            for u in self.get_unions():
                union_info = UnionInfo(name=u['name'], types=u['types'])
                self._unions.append(
                    UnionType(union_info, dependency_group=self.dependency_group))

        return self._unions

    @property
    def scalars(self):
        if not self._scalars:
            self._scalars = []

            for u in self.get_scalars():
                scalar_info = ScalarInfo(
                    name=u['name'], value=self.custom_scalars.get(u['name']))
                self._scalars.append(ScalarType(
                    scalar_info, dependency_group=self.dependency_group))

        return self._scalars

    @property
    def import_lines(self):
        return self.dependency_group.import_lines

    @property
    def file_representation(self):
        lines: List[str] = ['\n' * 3]

        if len(self.scalars) > 0:
            lines.extend(['## Scalars'] + ['\n' * 2])

            for s in self.scalars:
                lines.extend([s.file_representation] + ['\n' * 2])

        if len(self.unions) > 0:
            self.dependency_group.add_dependency(Dependency(
                imported_from='typing', dependency='Union'))
            lines.extend(['## Union Types'] + ['\n' * 2])

            for u in self.unions:
                lines.extend([u.file_representation] + ['\n' * 2])

        for b in self.sorted_blocks:
            lines.extend([b.file_representation] + ['\n' * 3])

            if b.name in RESOLVER_TYPES:
                for f in b.fields:
                    field: BlockField = f
                    if field.param_block and (len(field.param_block.fields) > 0 or self.generate_empty_params_types):
                        lines.extend(
                            [field.param_block.file_representation, '\n' * 3])

                    if field.result_definition:
                        lines.extend(
                            [field.result_definition, '\n' * 3])

        lines.insert(0, self.import_lines)

        return ''.join(lines)
