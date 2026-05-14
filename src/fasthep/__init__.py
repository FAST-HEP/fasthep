"""FAST-HEP meta package."""
from __future__ import annotations

__description__ = "Meta package for installing FAST-HEP workflow packages."

try:
    from ._version import version as __version__
except ModuleNotFoundError:
    __version__ = "0+unknown"
