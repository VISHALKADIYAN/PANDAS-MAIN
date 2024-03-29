import sys

from .accessor import register_path_accessor  # noqa

__all__ = [register_path_accessor]

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


__version__ = importlib_metadata.version(__name__.split(".", 1)[0])
