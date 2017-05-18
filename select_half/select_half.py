#python

# select_half.py
# Author: cignoir

import lx

fg = lx.eval("query layerservice layers ? fg")
verts = lx.eval("query layerservice verts ? all")

if verts is None:
    lx.out("No geometry")
else:
    for v in verts:
        pos = lx.eval("query layerservice vert.pos ? {0}".format(v))
        if pos[0] <= -0.00000001:
            lx.eval("select.element {0} vertex add index:{1}".format(fg,v))
