from .schema.schema import Schema

VERSION = (1, 0, 0)
__version__ = '.'.join(str(x) for x in VERSION)

__all__ = ['Schema']
