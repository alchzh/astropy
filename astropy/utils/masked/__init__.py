# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Built-in mask mixin class.

The design uses `Masked` as a factory class which automatically
generates new subclasses for any data class that is itself a
subclass of a predefined masked class, with `MaskedNDArray`
providing such a predefined class for `~numpy.ndarray`.
"""

from lazy_loader import attach_stub

__getattr__, __dir__, __all__ = attach_stub(__name__, __file__)
