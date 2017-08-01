# python
# resize_gap.py by ylaz dec 2014
# grab 2 verts & run
# or grab grab vert pairs for batch
# script resizes the gap w/t scaling the objects

main = lx.eval('query layerservice layer.index ? main')


def popup(var, type, dialog):
    if lx.eval("query scriptsysservice userValue.isDefined ? %(var)s" % vars()) == 0:
        lx.eval("user.defNew %(var)s %(type)s temporary" % vars())
    if dialog != None:
        lx.eval("user.value %(var)s" % vars())
    return lx.eval("user.value %(var)s ?" % vars())


distance = popup("distance", "float", "")

if not lx.eval('query scriptsysservice userValue.isDefined ? Axis'):
    lx.eval('user.defNew Axis integer')

lx.eval('user.def Axis list x;y;z')
lx.eval('user.value Axis')
Qaxis = lx.eval('user.value Axis ?')
lx.out(Qaxis)


def regap():
    verts = lx.eval('query layerservice verts ? selected')
    lx.out('verts', verts)
    pos1 = lx.eval('query layerservice vert.pos ? %s' % verts[0])
    pos2 = lx.eval('query layerservice vert.pos ? %s' % verts[1])
    gapX = abs(pos1[0] - pos2[0])
    gapY = abs(pos1[1] - pos2[1])
    gapZ = abs(pos1[2] - pos2[2])
    lx.out('pos1', pos1)
    lx.out('pos2', pos2)
    lx.out(gapX, gapY, gapZ)
    disX = gapX - distance
    disY = gapY - distance
    disZ = gapZ - distance
    lx.out('distance', distance)
    lx.eval('select.drop vertex')
    lx.command('select.element', layer=main,
               type='vertex', mode='set', index=verts[1])
    lx.eval('select.connect')
    lx.eval('tool.clearTask axis')
    lx.eval('tool.set TransformMove on')
    lx.eval('tool.reset')

    if Qaxis == 'x' and pos2[0] > pos1[0]:
        lx.eval('tool.attr xfrm.transform TX %s' % -(disX / 2))
    elif Qaxis == 'x' and pos2[0] < pos1[0]:
        lx.eval('tool.attr xfrm.transform TX %s' % (disX / 2))
    if Qaxis == 'y' and pos2[1] > pos1[1]:
        lx.eval('tool.attr xfrm.transform TY %s' % -(disY / 2))
    elif Qaxis == 'y' and pos2[1] < pos1[1]:
        lx.eval('tool.attr xfrm.transform TY %s' % (disY / 2))
    if Qaxis == 'z' and pos2[2] > pos1[2]:
        lx.eval('tool.attr xfrm.transform TZ %s' % -(disZ / 2))
    elif Qaxis == 'z' and pos2[2] < pos1[2]:
        lx.eval('tool.attr xfrm.transform TZ %s' % (disZ / 2))

    lx.eval('tool.doApply')
    lx.eval('tool.set TransformMove off')
    lx.eval('select.drop vertex')
    lx.command('select.element', layer=main,
               type='vertex', mode='set', index=verts[0])
    lx.eval('select.connect')
    lx.eval('tool.set TransformMove on')
    lx.eval('tool.reset')

    if Qaxis == 'x' and pos2[0] > pos1[0]:
        lx.eval('tool.attr xfrm.transform TX %s' % (disX / 2))
    elif Qaxis == 'x' and pos2[0] < pos1[0]:
        lx.eval('tool.attr xfrm.transform TX %s' % -(disX / 2))
    if Qaxis == 'y' and pos2[1] > pos1[1]:
        lx.eval('tool.attr xfrm.transform TY %s' % (disY / 2))
    elif Qaxis == 'y' and pos2[1] < pos1[1]:
        lx.eval('tool.attr xfrm.transform TY %s' % -(disY / 2))
    if Qaxis == 'z' and pos2[2] > pos1[2]:
        lx.eval('tool.attr xfrm.transform TZ %s' % (disZ / 2))
    elif Qaxis == 'z' and pos2[2] < pos1[2]:
        lx.eval('tool.attr xfrm.transform TZ %s' % -(disZ / 2))
    lx.eval('tool.doApply')
    lx.eval('tool.set TransformMove off')
    lx.eval('select.drop vertex')


iniverts = lx.eval('query layerservice verts ? selected')
lx.out('iniverts', iniverts)
items, chunk = iniverts, 2  # seq_No
verts2 = zip(*[iter(items)] * chunk)
lx.out('verts2', verts2)
count = len(verts2)
lx.out('count', count)
layer = lx.eval('query layerservice layer.index ? main')
lx.eval('select.drop vertex')

for i in range(count):
    lx.eval('select.element %s vertex set %s' % (layer, verts2[i][0]))
    lx.eval('select.element %s vertex add %s' % (layer, verts2[i][1]))
    regap()
    lx.eval('select.drop vertex')

for v in iniverts:
    lx.eval('select.element %s vertex add %s' % (layer, v))
