# select_half.py
# Author: https://github.com/cignoir

import modo

with modo.Mesh().geometry as geo:
    for v in geo.vertices:
        if v.position[0] < 0:
            v.select()