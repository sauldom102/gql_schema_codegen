import os
import subprocess
from pytest_snapshot.plugin import Snapshot


def get_current_file_path():
    return os.path.abspath(os.path.dirname(__file__))


def snap_test_schema(snapshot: Snapshot, schema_file: str, output_file: str):
    current_file_path = get_current_file_path()
    if current_file_path:
        snapshot.snapshot_dir = os.path.join(current_file_path, 'snapshots')

        schema_path = os.path.join(current_file_path, schema_file)
        output_path = os.path.join(current_file_path, 'snapshots', output_file)

        command = f"python -m gql_schema_codegen -c {os.path.join(current_file_path, 'config.yml')} -p {schema_path} -t {output_path}"
        output = subprocess.run(
            [command], capture_output=True, shell=True, text=True)
        output = output.stdout

        snapshot.assert_match(output, output_path)


def snap_test_url_schema(snapshot: Snapshot, schema_url: str, output_file: str):
    current_file_path = get_current_file_path()
    if current_file_path:
        snapshot.snapshot_dir = os.path.join(current_file_path, 'snapshots')

        output_path = os.path.join(current_file_path, 'snapshots', output_file)

        command = f"python -m gql_schema_codegen -c {os.path.join(current_file_path, 'config.yml')} -u {schema_url} -t {output_path}"
        output = subprocess.run(
            [command], capture_output=True, shell=True, text=True)
        output = output.stdout

        snapshot.assert_match(output, output_path)


def test_simple_schema_snapshot(snapshot: Snapshot):
    snap_test_schema(snapshot, 'test_schema.graphql', 'test_schema.py')


def test_countries_schema_snapshot(snapshot: Snapshot):
    snap_test_schema(snapshot, 'test_schema_countries.graphql',
                     'test_schema_countries.py')


def test_anilist_schema_snapshot(snapshot: Snapshot):
    snap_test_schema(snapshot, 'test_schema_anilist.graphql',
                     'test_schema_anilist.py')


def test_countries_v2_schema_snapshot(snapshot: Snapshot):
    snap_test_url_schema(snapshot, schema_url='https://countries-274616.ew.r.appspot.com/',
                         output_file='test_schema_countriesV2.py')


def test_gitlab_schema_snapshot(snapshot: Snapshot):
    snap_test_url_schema(snapshot, schema_url='https://gitlab.com/api/graphql',
                         output_file='test_schema_gitlab.py')


def test_pokeapi_schema_snapshot(snapshot: Snapshot):
    snap_test_schema(snapshot, 'test_schema_pokeapi.graphql',
                     output_file='test_schema_pokeapi.py')


def test_multidir_schema_snapshot(snapshot: Snapshot):
    snap_test_schema(snapshot, schema_file='test_schema_dir',
                     output_file='test_multidir_schema.py')
