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

landlow = (0,64,0)
landhigh = (116,182,133)
waterlow = (0,0,55)
waterhigh = (0,53,106)
mountlow = (147,157,167)
mounthigh = (226,223,216)

dimX = 1000
dimY = 2000
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

## It is assumed likely that the UV assigned faces are likely supplied
## such that any number of pixels will have unassigned/non computed
## heightmap values, thus the algorithm fills in for each pixel an actual
## heightmap value that in turn can be supplied to a colorizing routine
## The colorizing routine uses a gradient type palette set where
## a list of colors for terrain height conditions apply.  Any height
## for instance, between two terrain color height cutoff ranges are
## then linearly interpolated to determine color mixing between both
## such cutoffs.
