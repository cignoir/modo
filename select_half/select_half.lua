-- lua

-- SelectHalf.lua
-- Written by Joe Angell, Luxology LLC
-- Copyright (c) 2001-2005 Luxology, LLC. All Rights Reserved. Patents pending.

-- TestVertex():
-- Called by foreach() to test and select vertices
function TestVertex( index, value )
    local pos

    -- Get the position of the vertex
    pos = lxq(string.format("query layerservice vert.pos ? %i", value))
    if pos[1] < 0 then
        -- X position is less than 0; select it
        lx(string.format( "select.element layer:\"%i\" type:vertex mode:add index:%i", layers[1], value ) )
    end
end


-- "Select" the primary layer for querying via layer.name
layers = lxq( "query layerservice layers ? main" )

-- Get a list of all the vertices in the layer
verts = lxq( "query layerservice verts ? all" )
if verts == nil then
    error "No geometry"
end

-- Initialize the monitor
checkverts = table.getn(verts)

lxmonInit(checkverts)



-- Loop through all the vertices
table.foreach(verts, TestVertex)

for i=0,20 do
    for j=0,10000 do
        k = 1
    end

    if lxmonStep() == 0 then
        error( "User Break" )
    end

end
