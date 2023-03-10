import argparse
import sys

from .schema import Schema

parser = argparse.ArgumentParser(
    description="Generate python file with types from a GraphQL schema file."
)

parser.add_argument(
    "--schema-path",
    "-p",
    dest="schema_path",
    type=str,
    help="path of the schema file",
)

parser.add_argument(
    "--schema-url", "-u", dest="schema_url", type=str, help="url of the schema"
)

parser.add_argument(
    "--to-path",
    "-t",
    dest="to_path",
    type=str,
    help="wanted output file path",
)

parser.add_argument(
    "--config-file",
    "-c",
    dest="config_file",
    type=str,
    help="path of the config file in yaml format",
)

blocks = {
    "enum",
    "scalar",
    "type",
    "param_type",
    "input",
}

parser.add_argument(
    "-b",
    "--block",
    dest="blocks",
    action="append",
    choices=blocks,
    help="operate on these blocks differently",
)

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "--import",
    dest="import_blocks",
    help="module name from where to import --blocks",
)

group.add_argument(
    "--only",
    dest="only_blocks",
    action="store_true",
    help="only output blocks specified in --blocks",
)


args = parser.parse_args()

if __name__ == "__main__":
    s = Schema(
        path=args.schema_path,
        url=args.schema_url,
        config_file=args.config_file,
        blocks=args.blocks,
        import_blocks=args.import_blocks,
        only_blocks=args.only_blocks,
    )
    if args.to_path:
        file_representation = s.generate_type_file(args.to_path)
    else:
        sys.stdout.write(s.file_representation)
        sys.stdout.close()
