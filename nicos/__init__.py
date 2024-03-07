# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2024 by the NICOS contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Georg Brandl <g.brandl@fz-juelich.de>
#
# *****************************************************************************

"""
The nicos package contains all standard NICOS commands and devices.
"""

import sys
from logging import getLogger

# Provide the config object.
from nicos.configmod import config

# Determine our version(s).
from nicos._vendor.gitversion import get_git_version, get_nicos_version  # isort:skip
__version__ = nicos_version = get_nicos_version()

# Check for Python version 3.9+.
if sys.version_info[:2] < (3, 9):
    raise ImportError('NICOS requires Python 3.9 or higher')


# Create the nicos session object here to allow the import of submodules.
# The real class is set later.
class Session:
    log = getLogger('Nicos early logger')


session = Session()


def get_custom_version():
    try:
        return get_git_version(cwd=config.setup_package_path)
    except RuntimeError:
        return None


try:
    # numpy 1.14+ compat
    import numpy
    numpy.set_printoptions(sign=' ')
except Exception:
    pass
