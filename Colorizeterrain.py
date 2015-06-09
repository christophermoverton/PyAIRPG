import math
def bilinear_interpolation(x, y, points):
    '''Interpolate (x,y) from values associated with four points.

    The four points are a list of four triplets:  (x, y, value).
    The four points can be in any order.  They should form a rectangle.

        >>> bilinear_interpolation(12, 5.5,
        ...                        [(10, 4, 100),
        ...                         (20, 4, 200),
        ...                         (10, 6, 150),
        ...                         (20, 6, 300)])
        165.0

    '''
    # See formula at:  http://en.wikipedia.org/wiki/Bilinear_interpolation

    points = sorted(points)               # order points by x, then by y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0)

def lerpcolor(c1, c2, value):
	tcolor = [0,0,0]
	c1l = list(c1)
        c2l = list(c2)
	for g in range(3):
		if (c1l[g]>c2l[g])
			tcolor[g]=c2l[g]+(c1l[g]-c2l[g])*value

		else
			tcolor[g]=c1l[g]+(c2l[g]-c1l[g])*value
	
	return tuple(tcolor)

def getpixel(uvpixcoord ,dimX = dimX, dimY = dimY):
    px,py = uvpixcoord
##    px = ux*dimX
##    py = uy*dimY
    pyi = py*dimX*4
    pxi = px*4
    pix = pyi + pxi
    return (pix,pix+1,pix+2,pix+3)

def getpixelcoord(uv, dimX = dimX, dimY = dimY):
    ux,uy = uv
    return [ux*dimX, uy*dimY]

diff = maxheight-minheight,
flood=0.5  ## flood plain
mount=0.85 ##mountain level
	
flood*=diff
mount*=diff
landlow = (0,64,0)
landhigh = (116,182,133)
waterlow = (0,0,55)
waterhigh = (0,53,106)
mountlow = (147,157,167)
mounthigh = (226,223,216)

dimX = 1024
dimY = 2048
## this fills and existing blender image on the uv coordinates only
## it leaves non uv coordinate assigned to transparent alpha on non
## coordinate assigned pixel areas.
## Prerequisites for processing:
## This requires a coordinate terrain height dictionary
## This dictionary is vertex index keyed and height valued
## -This is called heightmap.
## -A dictionary called sphereproj is also needed, this is
##  a local coordinate keyed dictionary to UV coordinate value
## -A dictionary called vcoordtovindexrev dictionary.  This is
##  a vertex index keyed to local coordinate value dictionary.
## So three dictionaries indicated above are necessary for this algorithm.
## Also you will need to provide maximum and minimum heights

## It is assumed likely that the UV assigned faces are likely supplied
## such that any number of pixels will have unassigned/non computed
## heightmap values, thus the algorithm fills in for each pixel an actual
## heightmap value that in turn can be supplied to a colorizing routine
## The colorizing routine uses a gradient type palette set where
## a list of colors for terrain height conditions apply.  Any height
## for instance, between two terrain color height cutoff ranges are
## then linearly interpolated to determine color mixing between both
## such cutoffs.

## Iterate the faces to fill the pixel area
scn = bpy.context.scene
scn.objects.active = ob
ob.select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bm = bmesh.from_edit_mesh(ob.data)
D = bpy.data
 
# BlendDataImages.new(name, width, height, alpha=False, float_buffer=False)
image_object = D.images.new(name='pixeltest', dimX, dimY)
for f in bm.faces:
    verts = []
    vertmatch = False
    for l in f.verts:
        ## get vert index boundaries
        if l.index in verts:
            vertmatch = True
            break
        verts.append(l.index)
        
    ## get uv coord
    if vertmatch:
        continue
    uvcoords = []
    uvheights = []
    for vi in verts:
        vcoord = vcoordtovindexrev[vind]
        uvcoord = sphereproj[vcoord]
        u,v = uvcoord
        uvcoords.append(list(uvcoord))
        uvheights.append([u,v,heightmap[vi]])
    ## get min max coords
    sortset = uvcoords[0:len(uvcoords)]
    sortset.sort(key=lambda tup: tup[0])
    minset = sortset[0:2]
    maxset = sortset[2:4]
    minset.sort(key=lambda tup:tup[1])
    maxset.sort(key=lambda tup:tup[1])
    minuvcoord = minset[0]
    maxuvcoord = maxset[1]
    ## now we convert min max coords to pixel coordinates
    minpixcoord = getpixelcoord(minuvcoord)
    maxpixcoord = getpixelcoord(maxuvcoord)
    ## now we iterate the set of pixels from minpix x to maxpix along x
    ## and minpix y to maxpix y
    pixcoord = minpixcoord
    for j in range(minpixcoord[1],maxpixcoord[1]):
        for i in range(minpixcoord[0],maxpixcoord[0]):
            h = bilinear_interpolation(i, j, points) ## bilinearly interpolated height for uv
            if (h<flood):
                newcolor=colorlerp(waterlow,waterhigh,h/flood)
            elif (h>mount):
                newcolor=colorlerp(mountlow,mounthigh,(h-mount)/(diff-mount))
            else:
                newcolor=colorlerp(landlow,landhigh,(h-flood)/(mount-flood));
            
