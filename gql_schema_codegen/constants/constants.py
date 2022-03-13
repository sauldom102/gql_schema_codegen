from typing import Dict


VALUE_TYPES: Dict[str, str] = {
    'ID': 'str',
    'String': 'str',
    'Int': 'int',
    'Float': 'float',
    'Boolean': 'bool',
}

BLOCK_PATTERN = r'(?P<type>type|input|enum|interface)\s(?P<name>[\w_]+)\s(implements\s(?P<implements>[\w_\s&]+)\s)?\{(?P<fields>[^}]+)\}\n?'

FIELD_PATTERN = r'(?P<name>[\w_]+)(\((?P<params>[^)]+)\))?(\:\s(?P<value_type>([\w\[\]_!]+)))?.*\n'

UNION_PATTERN = r'^union\s(?P<name>[\w_]+)\s=\s(?P<types>[\w\s,|]+)$'

SCALAR_PATTERN = r'^scalar\s(?P<name>[\w_]+)$'

DIRECTIVE_PATTERN = r'directive[\s\n\w:_|@()\[\]-]+\son\s[\w_]+'

DIRECTIVE_USAGE_PATTERN = r'@[^(]+\(([^)])+\)'

RESOLVER_TYPES = ['Query', 'Mutation', 'Subscription']
