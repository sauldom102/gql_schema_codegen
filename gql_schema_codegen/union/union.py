import re
from typing import NamedTuple
from ..dependency import DependencyGroup, Dependency
from ..base import BaseInfo


class UnionInfo(NamedTuple):
    name: str
    types: str


class UnionType(BaseInfo):

    def __init__(self, info: UnionInfo, dependency_group: DependencyGroup) -> None:
        super().__init__(info)
        self.dependency_group = dependency_group

    @property
    def separated_types(self):
        return re.sub(r'[^\w\|]', '', self.types).split('|')

    @property
    def cleaned_types(self):
        return ', '.join(map(lambda t: f"'{t}'", self.separated_types))

    @property
    def file_representation(self):
        if len(self.separated_types) == 1:
            only_type = self.separated_types[0]
            return f"{self.name} = ClassVar['{only_type}']"

        return f"{self.name} = Union[{self.cleaned_types}]"

    def __repr__(self) -> str:
        return self.file_representation
