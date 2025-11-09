# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2025 by the NICOS contributors (see AUTHORS)
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
#   Jens Krüger <jens.krueger@frm2.tum.de>
#
# *****************************************************************************

"""NICOS Garfield magnet test suite."""

import pytest

from nicos.core.errors import ConfigurationError

session_setup = 'garfield'


def assertPos(pos1, pos2):
    for v1, v2 in zip(pos1, pos2):
        assert v1 == pytest.approx(v2, abs=1e-3)


@pytest.mark.parametrize(['dev', 'symmetry', 'target', 'abslimits', 'current'], [
    ('magnet', 'symmetric', 0.2, (-0.2344, 0.2344), 81.898),
    ('magnet', 'symmetric', -0.2, (-0.2344, 0.2344), -81.898),
    ('magnet', 'short', 0, (0, 0), 0),
    ('magnet', 'unsymmetric', 0.15, (-0.1820, 0.1820), 77.418),
    ('rmagnet', 'symmetric', 0.2, (-0.2344, 0.2344), 81.898),
])
def test_magnet(session, dev, symmetry, target, abslimits, current):
    magnet = session.getDevice(dev)
    currentdev = magnet._attached_currentsource
    symmetrydev = magnet._attached_symmetry
    pytest.raises(ConfigurationError, setattr, magnet, 'calibration', (1, 0, 0, 0, 0))

    # the default formula is B(I) = c0*I + c1*erf(c2*I) + c3*atan(c4*I)
    symmetrydev.maw(symmetry)
    assert currentdev.abslimits == (-100, 100)
    assertPos(magnet.abslimits, abslimits)
    magnet.maw(target)
    assert magnet.read(0) == pytest.approx(target, abs=1e-6)
    assert currentdev.read(0) == pytest.approx(current, abs=1e-3)

    magnet.reset()
