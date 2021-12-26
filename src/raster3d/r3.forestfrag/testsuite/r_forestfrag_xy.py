#!/usr/bin/env python

# TODO: create a 3D version of this to test r3.forestfrag

############################################################################
#
# MODULE:        r_forestfrag_xy
# AUTHOR:        Vaclav Petras
# PURPOSE:       Test with complete but small ref output (diff windows)
# COPYRIGHT:     (C) 2016 by Vaclav Petras and the GRASS Development Team
#
#                This program is free software under the GNU General Public
#                License (>=v2). Read the file COPYING that comes with GRASS
#                for details.
#
#############################################################################


from grass.gunittest.case import TestCase
from grass.gunittest.main import test

# this is in fact taken from the NC SPM Location landclass96 raster map

FOREST = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 1
0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 1 0 1 1 1 1 1 1 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0
"""

FRAG_3 = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 2 2 2 1 0 0 0 1
0 0 0 3 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 0 0 0 0 0 0 0 0 0
0 0 0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 0 0 0 0 0 0 0 0 0
0 3 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 0 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 0 0 0 1 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 3 4 4 4 4 5 5 4 4 0 0 4 4 0 0 0 0
0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 0 0 0 2 0 4 5 5 5 4 4 4 4 4 4 2 0 0
0 2 3 3 3 3 4 4 5 5 5 5 5 5 4 4 0 0 0 0 0 0 3 5 5 5 5 5 5 5 5 4 2 0 0
0 0 0 0 0 0 0 4 5 5 5 5 5 5 4 0 0 2 3 3 2 0 4 5 5 4 4 3 3 3 3 2 0 0 0
0 0 0 0 0 0 0 3 5 5 5 5 5 5 4 4 4 4 5 5 4 4 4 5 4 4 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 0 0 0 0 0 0 0 0 0 0
0 2 3 3 3 3 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 0 0 0 0 0 0 0 0 0 0 0
0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 0 0 0 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 2 0 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 0 0 0 0 0 0
0 3 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 0 0 0 0 0
0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 1 0 1 0
"""

FRAG_5 = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 2 1 1 1 0 0 0 1
0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0
0 0 0 3 3 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 0 0 0 0 0 0 0 0 0
0 0 3 3 3 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 0 0 0 0 0 0 0 0 0
0 0 3 3 4 5 5 5 5 5 5 5 5 5 5 4 3 3 4 3 4 4 4 4 3 3 0 0 0 1 0 0 0 0 0
0 0 4 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 3 3 3 3 4 3 3 3 3 0 0 2 2 0 0 0 0
0 0 3 3 3 3 3 3 4 5 5 5 5 4 3 4 4 0 0 0 4 0 4 3 4 3 3 6 3 3 3 2 1 0 0
0 2 2 3 3 3 3 3 3 5 5 5 5 4 4 4 0 0 0 0 0 0 4 4 4 4 3 4 3 3 3 2 1 0 0
0 0 0 0 0 0 0 3 3 5 5 5 5 4 4 0 0 3 3 3 4 0 4 3 3 3 3 3 3 3 2 2 0 0 0
0 0 0 0 0 0 0 3 4 5 5 5 5 4 4 4 4 3 3 3 3 4 4 3 3 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 5 5 5 5 4 3 4 4 3 4 4 4 4 4 3 3 0 0 0 0 0 0 0 0 0 0
0 2 2 3 3 3 3 3 3 5 5 5 5 5 5 5 5 5 5 5 5 5 4 6 0 0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 3 3 3 4 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 0 0 0 0 0 0 0 0 0 0 0
0 0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 2 0 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 2 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 0 0 0 0 0 0 0
0 0 3 3 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 0 0 0 0 0 0
0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 2 0 0 0 0 0
0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 2 1 0 1 0
"""

FRAG_7 = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 2 2 1 1 1 0 0 0 1
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 3 3 3 5 5 5 5 5 5 5 5 4 3 3 3 4 4 4 4 4 4 3 3 0 0 0 0 0 0 0 0 0
0 0 0 3 3 3 5 5 5 5 5 5 5 4 3 3 3 3 3 3 3 3 3 3 3 3 0 0 0 1 0 0 0 0 0
0 0 0 3 3 3 3 3 3 4 5 5 4 3 3 3 3 4 3 4 4 4 4 4 3 3 3 0 0 2 2 0 0 0 0
0 0 0 3 3 3 3 3 3 3 5 5 4 4 4 4 4 0 0 0 4 0 4 4 3 3 3 3 2 2 2 1 1 0 0
0 2 2 2 3 3 3 3 3 3 5 5 4 4 4 4 0 0 0 0 0 0 4 4 3 3 3 3 2 2 2 1 1 0 0
0 0 0 0 0 0 0 3 3 3 5 5 4 4 4 0 0 4 4 4 4 0 4 3 3 3 3 2 2 2 1 1 0 0 0
0 0 0 0 0 0 0 3 3 3 5 5 4 4 4 3 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 5 5 4 3 4 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0
0 2 2 2 3 3 3 3 3 3 5 5 4 3 4 4 4 4 3 4 4 4 4 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 3 3 3 3 3 3 3 5 5 5 5 5 5 5 5 5 5 5 4 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 3 3 3 3 3 3 4 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 2 0 0 0 0 0 0 0 0 0
0 0 0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 3 3 2 0 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 3 2 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 0 0 0 0 0 0 0
0 0 0 3 3 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 2 2 1 0 1 0
"""

FRAG_9 = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 2 2 1 1 1 0 0 0 1
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 4 4 3 3 3 3 3 3 4 3 3 3 3 3 3 3 0 0 0 2 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 3 4 4 4 4 3 4 4 4 4 4 3 3 3 3 3 3 0 0 2 1 0 0 0 0
2 2 0 0 3 3 3 3 3 3 3 4 4 4 4 3 4 0 0 0 4 0 3 3 3 3 3 2 2 1 1 1 1 0 0
0 0 0 0 3 3 3 3 3 3 3 4 4 4 4 3 0 0 0 0 0 0 3 3 3 3 3 2 2 1 1 1 1 0 0
0 0 0 0 0 0 0 3 3 3 3 4 4 4 4 0 0 4 4 4 4 0 3 3 3 3 3 2 2 1 1 1 0 0 0
0 0 0 0 0 0 0 3 3 3 3 4 4 4 4 3 4 4 4 4 4 3 3 3 3 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 3 4 4 4 3 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 3 4 3 4 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 3 4 3 4 4 4 4 4 4 4 4 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 3 5 5 5 5 5 5 5 5 5 4 3 3 3 3 2 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 4 5 5 5 5 5 5 5 5 5 4 3 3 3 3 3 2 0 0 0 0 0 0 0 0
0 0 0 0 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 3 3 3 2 2 0 0 0 0 0 0 0
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 3 3 3 2 0 0 0 0 0 0 0
0 0 0 0 3 3 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 3 3 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 2 2 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 2 2 1 0 1 0
"""

FRAG_13 = """\
north: 220105.5
south: 219478.5
east: 634609.5
west: 633612
rows: 22
cols: 35
0 0 0 0 0 0 0 0 0 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 0 0 0 1
0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 4 0 0 0 3 0 3 3 3 3 2 2 2 2 1 1 1 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 3 3 3 3 2 2 2 1 1 1 1 0 0
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 0 0 4 4 3 3 0 3 3 3 3 2 2 2 1 1 1 0 0 0
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 4 4 4 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 4 4 4 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 4 4 4 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 4 4 4 4 4 4 3 3 3 3 3 3 3 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3 3 5 5 5 5 5 4 3 3 3 3 3 3 3 2 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 5 5 5 5 5 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 0 2 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0 0 2 2 2 2 0 1 0
"""


class TestForestFragXY(TestCase):
    # TODO: replace by unified handing of maps
    to_remove = []
    forest = "rff_test_forest"
    forest_frag = "rff_test_forest_frag"
    forest_frag_ref = "rff_test_forest_frag_ref"

    def setUp(self):
        self.use_temp_region()
        self.runModule("r.in.ascii", input="-", stdin_=FOREST, output=self.forest)
        self.to_remove.append(self.forest)
        self.runModule("g.region", raster=self.forest)

    def tearDown(self):
        self.del_temp_region()
        if self.to_remove:
            self.runModule(
                "g.remove",
                flags="f",
                type="raster",
                name=",".join(self.to_remove),
                verbose=True,
            )

    def forest_frag_general(self, window, reference):
        self.runModule(
            "r.in.ascii", input="-", stdin_=reference, output=self.forest_frag_ref
        )
        self.to_remove.append(self.forest_frag_ref)
        # just check if the reference is all right
        theoretical_min = 0
        theoretical_max = 6
        self.assertRasterMinMax(
            self.forest_frag_ref, refmin=theoretical_min, refmax=theoretical_max
        )
        ref_univar = dict(n=770, null_cells=0, cells=770)
        self.assertRasterFitsUnivar(
            raster=self.forest_frag_ref, reference=ref_univar, precision=0
        )

        # actually run the module
        self.assertModule(
            "r.forestfrag", input=self.forest, output=self.forest_frag, window=window
        )
        self.assertRasterExists(self.forest_frag)
        self.to_remove.append(self.forest_frag)

        # check the basic properties
        self.assertRasterMinMax(
            self.forest_frag, refmin=theoretical_min, refmax=theoretical_max
        )
        self.assertRasterFitsUnivar(
            raster=self.forest_frag, reference=ref_univar, precision=0
        )

        # check cell by cell
        self.assertRastersNoDifference(
            actual=self.forest_frag, reference=self.forest_frag_ref, precision=0
        )  # it's CELL type

    def test_3(self):
        self.forest_frag_general(3, FRAG_3)

    def test_5(self):
        self.forest_frag_general(5, FRAG_5)

    def test_7(self):
        self.forest_frag_general(7, FRAG_7)

    def test_9(self):
        self.forest_frag_general(9, FRAG_9)

    def test_13(self):
        self.forest_frag_general(13, FRAG_13)


if __name__ == "__main__":
    test()