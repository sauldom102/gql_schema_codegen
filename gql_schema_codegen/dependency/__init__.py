from .dependency import (Dependency, DependencyGroup,
                         get_interface_dependencies,
                         remove_interface_dependencies,
                         update_interface_dependencies)

__all__ = [
    "Dependency",
    "DependencyGroup",
    "get_interface_dependencies",
    "update_interface_dependencies",
    "remove_interface_dependencies",
]
