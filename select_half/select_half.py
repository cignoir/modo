#python

# select_half.py
# Author: cignoir

import lx

layer_index = lx.eval("query layerservice layer.index ? main")
verts = lx.eval("query layerservice verts ? all")

if verts is None:
    lx.out("No geometry")
else:
    for vert_index, vert in enumerate(verts):
        if vert.pos[1] < 0:
            lx.eval("select.element layer:\"%i\" type:vertex mode:add index:%i" % (layer_index, vert_index))
