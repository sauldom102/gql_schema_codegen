from itertools import groupby
from typing import List, NamedTuple, Set


class Dependency(NamedTuple):
    imported_from: str
    dependency: str


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
