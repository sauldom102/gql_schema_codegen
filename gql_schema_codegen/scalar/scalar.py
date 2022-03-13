from typing import NamedTuple, Optional
from ..constants.constants import VALUE_TYPES
from ..dependency.dependency import Dependency, DependencyGroup
from ..base import BaseInfo


class ScalarInfo(NamedTuple):
    name: str
    value: Optional[str]


class ScalarType(BaseInfo):

    def __init__(self, info: ScalarInfo, dependency_group: DependencyGroup) -> None:
        super().__init__(info)
        self.dependency_group = dependency_group

    @property
    def file_representation(self):
        if type(self.value) is not str:
            self.dependency_group.add_dependency(
                Dependency(imported_from='typing', dependency='Any'))

            return f"{self.name} = Any"

        if self.value in list(VALUE_TYPES.values()):
            return f"{self.name} = {self.value}"

        self.dependency_group.add_dependency(
            Dependency(imported_from='typing', dependency='ClassVar'))

        return f"{self.name} = ClassVar['{self.value}']"

    def __repr__(self) -> str:
        return self.file_representation
