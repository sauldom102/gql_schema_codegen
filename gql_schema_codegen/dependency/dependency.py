from itertools import groupby
from typing import Dict, List, NamedTuple, Set


class Dependency(NamedTuple):
    imported_from: str
    dependency: str


INTERMEDIATE_INTERFACES: Dict[str, str] = {}


def get_interface_dependencies():
    return INTERMEDIATE_INTERFACES


def update_interface_dependencies(config_file_content):
    global INTERMEDIATE_INTERFACES
    if isinstance(config_file_content, dict):
        data = config_file_content.get("interfaceInheritance")
        if isinstance(data, dict):
            INTERMEDIATE_INTERFACES = data


def remove_interface_dependencies(
    interfaces: List[str],
    intermediate_interfaces: Dict[str, str] = {},
) -> List[str]:
    """Filter all dependencies from intermediate interfaces

    Assumes that all keys in intermediate_interfaces are leaf nodes and
    returns all other parent interfaces from a given list

    Intemediate interfaces in GraphQL implement other interfaces. This is part
    of the spec (see https://github.com/graphql/graphql-spec/pull/373)
    but not implemented in all clients yet (e.g., neo4j)
    Thus we are parsing intermediate interfaces in scalars.yml so as to emit
    proper python code without relying on the graphql schema being correct


    >>> remove_interface_dependencies(['t1', 't2', 'i1', 'i2', 't3'], {'i1':'i2'})
    ['t1', 't2', 'i1', 't3']

    >>> remove_interface_dependencies(['t1', 't2', 't3'], {})
    ['t1', 't2', 't3']

    >>> remove_interface_dependencies(['t1', 't2', 'i1', 'i2', 'i3', 't3'], \
                                      {'i1':'i2', 'i2': 'i3'})
    ['t1', 't2', 'i1', 't3']

    >>> remove_interface_dependencies(['t1', 't2', 'i1', 'i2', 'i3', \
                                       'ni1', 'ni2', 't3'], \
                                      {'i1':'i2', 'i2': 'i3', 'ni1':'ni2'})
    ['t1', 't2', 'i1', 'ni1', 't3']
    """
    deps: Set[str] = set()
    intermediate_interfaces = intermediate_interfaces or INTERMEDIATE_INTERFACES
    for i in interfaces:
        if i not in intermediate_interfaces:
            # this is not an intermediate interface, thus we are keeping it
            # as a dependency
            continue

        # add the parent dependency to the list of tracked dependencies:
        deps.add(intermediate_interfaces[i])

    # transitively fetch all dependencies
    seen: Set[str] = set()
    while deps:
        d = deps.pop()
        if d in seen:
            continue
        if d in intermediate_interfaces:
            deps.add(intermediate_interfaces[d])
        seen.add(d)

    return list(filter(lambda x: x not in seen, interfaces))


class DependencyGroup:
    def __init__(
        self, deps: Set[Dependency] = set(), direct_deps: Set[str] = set()
    ) -> None:
        self.deps = set(deps)
        self.direct_deps = set(direct_deps)

    def add_dependency(self, dependency: Dependency) -> None:
        self.deps.add(dependency)

    def add_direct_dependency(self, dependency: str) -> None:
        self.direct_deps.add(dependency)

    @property
    def import_lines(self):
        lines: List[str] = []
        list_of_deps = sorted(
            list(self.deps), key=lambda d: f"{d.imported_from} - {d.dependency}"
        )
        grouped_deps = groupby(list_of_deps, lambda d: d.imported_from)

        for dep_from, deps in grouped_deps:
            dep_group_deps = [d.dependency for d in deps]
            lines.append(f"from {dep_from} import {', '.join(dep_group_deps)}")

        for dd in sorted(list(self.direct_deps)):
            lines.append(f"import {dd}")

        return "\n".join(lines)
