import argparse
import sys

from .schema import Schema


parser = argparse.ArgumentParser(
    description="Generate python file with types from a  GraphQL schema file."
)

parser.add_argument(
    "--schema-path",
    "-p",
    dest="schema_path",
    type=str,
    help="path of the schema file (default: schema.graphql)",
)

parser.add_argument(
    "--schema-url", "-u", dest="schema_url", type=str, help="url of the schema"
)

parser.add_argument(
    "--to-path",
    "-t",
    dest="to_path",
    type=str,
    help="wanted output file path (default: schema_types.py)",
)

parser.add_argument(
    "--config-file",
    "-c",
    dest="config_file",
    type=str,
    default="gql_schema_codegen.config.yml",
    help="path of the config file in yaml format (default: gql_schema_codegen.config.yml)",
)

parser.add_argument(
    "--enum-only",
    dest="enum_only",
    action="store_true",
    help="whether to generate only enums",
)

parser.add_argument(
    "--enum-module",
    dest="enum_module",
    type=str,
    help="module name from where to import eums. if not provided enums are generated in-place",
)


args = parser.parse_args()

if __name__ == "__main__":
    s = Schema(
        path=args.schema_path,
        url=args.schema_url,
        config_file=args.config_file,
        enum_only=args.enum_only,
        enum_module=args.enum_module,
    )
    if args.to_path:
        file_representation = s.generate_type_file(args.to_path)
    else:
        sys.stdout.write(s.file_representation)
        sys.stdout.close()
