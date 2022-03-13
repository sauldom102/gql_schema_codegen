import sys
import argparse
from .schema import Schema

parser = argparse.ArgumentParser(
    description='Generate python file with types from a  GraphQL schema file.')

parser.add_argument('--schema-path', '-p', dest='schema_path', type=str,
                    help='path of the schema file (default: schema.graphql)')

parser.add_argument('--schema-url', '-u', dest='schema_url', type=str,
                    help='url of the schema')

parser.add_argument('--to-path', '-t', dest='to_path', type=str, default='generated_schema_types.py',
                    help='wanted output file path (default: schema_types.py)')

parser.add_argument('--config-file', '-c', dest='config_file', type=str, default='gql_schema_codegen.config.yml',
                    help='path of the config file in yaml format (default: gql_schema_codegen.config.yml)')


args = parser.parse_args()

if __name__ == '__main__':
    schema_path, schema_url, to_path, config_file = args.schema_path, args.schema_url, args.to_path, args.config_file

    s = Schema(path=schema_path, url=schema_url, config_file=config_file)
    file_representation = s.generate_type_file(to_path)

    sys.stdout.write(file_representation)
    sys.stdout.close()
