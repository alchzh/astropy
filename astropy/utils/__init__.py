# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This subpackage contains developer-oriented utilities used by Astropy.

Public functions and classes in this subpackage are safe to be used by other
packages, but this subpackage is for utilities that are primarily of use for
developers or to implement python hacks.

This subpackage also includes the ``astropy.utils.compat`` package,
which houses utilities that provide compatibility and bugfixes across
all versions of Python that Astropy supports. However, the content of this
module is solely for internal use of ``astropy`` and subject to changes
without deprecations. Do not use it in external packages or code.

"""

from lazy_loader import attach_stub

__getattr__, __dir__, __all__ = attach_stub(__name__, __file__)
