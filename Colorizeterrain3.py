import math
import random
import bpy,bmesh
from mathutils import *
from mathutils.noise import *
from math import *
global dimX,dimY, NORMFAC
BICUBIC = False ## don't make True not enabled at the moment
NORMFAC = 1
dimX = 1024
dimY = 1024
colormap = {}
landlow = (0,64,0)
landhigh = (116,182,133)
landlow_rock = (82,87,81)
landhigh_rock = (146,179,134)
landlow_rock2 = (207,197,169)
landhigh_rock2 = (87,83,71)
landlow_dirt = (156,158,104)
landhigh_dirt = (199,201,135)
waterlow = (0,0,55)
waterlow2 = (162,164,245)
waterhigh = (0,53,106)
waterhigh2 = (164,232,139)
mountlow = (147,157,167)
mounthigh = (226,223,216)
rock = (145,148,141)
dark_rock = (94,94,94)
light_grass = (122,227,84)
dark_grass = (94,168,67)
nsize = 150.0 ## ranges from .01 to 10000 (used in fractalizing terrain coloring)
nsize2 = 40.0
nsize3 = 40.0 ## high water fractal texturing
nbasis = 3 ## default 0 for Blender
nbasis2 = 3
nbasis3 = 3
rseed = 201
featherstepval = .01
## table of cubic falloff polys (given with coefficients)
## starting point is (0,0) end point is (cf_key,1)
cf = {.05:[-4384.9,75.6728,27.1786,-1.11022e-16],
.1:[-83.3021,-72.8482,18.1178,0.0],
.2:[-87.1624,15.5496, 5.37658,2.22045e-16],
.3:[-19.0496,1.63399,4.5576,0.0],
.4:[-2.99053,-3.03613,4.19294,-2.22045e-16],
.5:[0.646465,-4.49285,4.08481,-2.22045e-16],
.6:[1.60934,-4.94142,4.05216,0.0],
.7:[2.32556,-5.33564,4.02399,0.0]}
CFK1 = .3
CFK2 = .1

## normal thresholding module how it works:
## Thresholding modules are housed in a list nested dictionary called
## TM
## any modules are read and unpacked and accordingly applied in sequential
## order based upon its 'sequence' identifier.
## Modules need have the following key information:
## 'Landtype' specified either 'Flood', 'Land', 'Mount'
## 'Type' specified either 'Height', or 'Normal'
## 'TBracket' or Threshold bracket range these need supplied ordered csale
## 2 tuple 0 <= value <= 1.  Note: any overlap in the bracketing range
## from one module to the next on the same landtype will lead to mixing
## of modules which may or may not be what you are looking for.  If you
## want distinct textures for specific normal ranges you will need to keep
## the Tbracket ranges non overlapping for min max cscale ranges chosen
## for each module of the same landtype.  Note: TBracket set [0,1] means
## thresholding is off (or covers the range).
## 'Fractal'  boolean means color mixing is either fractalized between
## on the modules 1d polar spectrum or not.  If not chosen mixing method is
## by default given (ratio of measured distance of a normal relative to
## threshold relative to the maximum normal distance for such threshold range)
## Modules will at a basis at least a 2 tone 1 dimensional polar spectrum.
## Meaning these will be assigned at least two color tones at either polar end.
## Position values of any color tone range from 0 to 1.
## Open poles and all positions between such applied to the nearest (to pole)
## color position will be the same color as such as nearest neighboring color.
## Linear interpolation will apply in so far as mixing between colors.
## 'Colors'  is a 2 dimensional list.  A nested list contains a rgb color
## assignment 3-tuple and its position marker 
## 'nsize' (applies if 'Fractal' is true) This sets the fractal size.
## 'nbasis' ('Fractal' true).  This selects the basis of the fractal (see below).
## 'lacunarity' ('Fractal' true).  This sets the lacunarity of the fractal noise.
## 'depth' ('Fractal' true).  Depth (see below)
## 'dimension' ('Fractal true).  see below.
## 'Name' This is non used in terrain generation but kept for organizational
## purpose.
## 'Id'. This is the corresponding driver id for color mixing.
## It is noted that internal color mixing is given with all the internal
## instructions given by the NTMC module itself, but this doesn't provide
## external mixing instructions for a given output color determination
## of the module.
##  External mixing where a color value need be done by mixing module.
## Threshold modules are basis units that compute what need be done before
## color information is aggregated further by the mixing modules. Calls
## to TM are done especially with calls to fractalization for color
## mixing that are not handled by the color mixing modules directly (no
## driver interface provided here).

## Mixing Modules (MM)
## Dictionary key: Module ID 
## All mixing module ins and outs are routed through ColorInOut module.
## Mixing Modules is a list dictionary with the following properties:
## 'Id'  Module Id.
## 'Ins' Module input identifiers are provided here.  2 are necessary to
## proper functioning of the module.  These are 2 tuple defined.
## 'Outs' Module output identifiers here.  Minimum of 1 supplied.
## 'Type'  Type is given by one of the following:
##  'Multiply, Screen, Overlay, Hard light, Soft Light, Dodge, Burn,
##   Divide, Addition, Subtract, Difference, Darken Only, Lighten Only,
##   Normal (colorlerp), Normal2 (colorlerp2)'
## 'FactorType' either 'fixed' or 'variable', or 'falloff' 
## 'FactorVar' (if FactorType set 'variable' only) set either 'normal' or
## 'height', 'normalT' (normal threshold), or 'heightT' (height threshold)   
## 'Factor' (FactorType set 'fixed' only).
##  This is a real value from 0 to 1.  The factor amount for the mixing
## type.
## 'Falloff'. (FactorType 'falloff' only).
## This is the amount of feathering applied for a given threshold
## you must use the cf ranges specified below.  You can choose, .05, .1, .2
## to .7.  The cf value must exist in the cf dictionary (see below).
## Setting 'Falloff' to 0 (zero) otherwise, specifies that mixing falloff
## is turned off.
## 'Landtype' is given by 'Flood, Land, or Mount'
## All 'variable' factor is given by 'RH(N)D/TH(N)D' (ratio of measured
## height (height threshold) or normal (normal threshold) distance or 
## 
## on a given height/normal land type range relative to total height/normal
## (threshold) distance for such land type range...ratios given by 'threshold'
## are only as given by 'heightT' or 'normalT' FactorVar 

## ColorInOut Module (CIOM)
## dictionary
## 'ModuleID'  This is the module id for a given color input assignement
## Note any module ID is given either by a threshold module or mixing module.
## so it is likely important that any identifier provided for either module
## type neither has id overlap.
##  'RGB' is the rgb standard 3 tuple given value (non normalized).
## ColorInOut Module is a dictionary database for the mixing driver.

## Mixing Driver (MD)
## ordered list
## given by a operating mixing module ID sequence.  It is up to a user to supply
## a valid sequence so that all chain interdependencies in a given computation
## set are appropriately handled...if this were given in a visual context,
## it is up to the user supplying a valid and properly linked chain node from
## one mixing module node to the next.

## Node Chains (NCs)
## Dictionary:  key - Threshold module id - Mixing node chain[mixing id list]
## These are a given layer between the mixing driver and threshold modules
## The way that these are structured is 'if, then'  That is 'if' threshold
## module ID is computed 'then' the following mixing module nodes are linked
## to this tm.

## DirectColorInput(DCI)
##  This allows one to directly input colors into the ColorInOut Module
## so that it is stored with a reference identifier in the CIOM.  That is,
## an identifier that is given either as a result of TM computation or a
## MM computation.

## Schematics of overall terrain colorization goes as follows:
## unpack threshold modules having placed these into three categories:
## 'flood' modules, 'land' modules, 'mount' modules.
## Mixing modules will also be unpacked, these will contain both
## input and output channel information along with any sequence assingnment
## for computation work (to ensure necessary data is put in place) before
## sequentially passing to such module for computation. 
## Do everything as necessary in preparation as shown below prior to pixel
## by pixel computation of rgb terrain colorization routine.
##  In pixel by pixel routines, extract height and normal.
## Height data determines which land type modules are used computation wise.
## 'Land' modules will use all modules computation wise (for threshold
## feathering between land types).
## All threshold module computations and any subsequent mixing module
## computations will have data pathed to a ColorInOut module, and also
## trigger a pixel mixer driver configuration through the NodeChains dictionary.
## ColorInOut module is basically identified computed work already having
## been task accomplished as given by its parent module identifier (whether
## such parent is a 'Threshold module' or a 'Mixing module').
## The ColorInOut module will be in part used by the Mixing Driver which
## outside of preliminary threshold module 'basis' work will be the overarching
## driver for sequentially producing a given terrain pixel output.  
## The mixing driver is read on a simple loop iterator.  The mixing driver loop
## iterator traverses the MixingModule ID sequence.  The appropriate
## Mixing Module is loaded.  This data is passed to mixing module function.
## repeating the process until the Mixing driver loop is finished.
## Mixing Modules may have variably written per pixel given instructions
## that is, each driver instruction is not the same for pixel to pixel,
## if for instance, thresholding dictates that added color mixing schemes
## need exist for a given pixel position. Once pixel computation is complete
## we reinitialize the ColorInOut module.

##("0","Blender","Blender"),
##                ("1","Perlin","Perlin"),
##                ("2","NewPerlin","NewPerlin"),
##                ("3","Voronoi_F1","Voronoi_F1"),
##                ("4","Voronoi_F2","Voronoi_F2"),
##                ("5","Voronoi_F3","Voronoi_F3"),
##                ("6","Voronoi_F4","Voronoi_F4"),
##                ("7","Voronoi_F2-F1","Voronoi_F2-F1"),
##                ("8","Voronoi Crackle","Voronoi Crackle"),
##                ("9","Cellnoise","Cellnoise")]
lacunarity = 2.1 ## default is 2 with min = .01 to max = 6.0
lacunarity2 = 2.2
lacunarity3 = 2.1
depth = 10.0 ## min =1 to max =16 default 6 number of fbm frequencies
## this is the frequency of fractional brownian motion (important fractalizing
## characteristic).
depth2 = 10.0
depth3 = 10.0
dimension = 1.0 ## min = .01 to max = 2.0 default 1.0 fractal dimension
## of the roughest areas
    # origin
dimension2 = 1.1
dimension3 = 1.1
if rseed == 0:
     origin = 0.0,0.0,0.0
     origin_x = 0.0
     origin_y = 0.0
     origin_z = 0.0
else:
# randomise origin
     seed_set( rseed )
     origin = random_unit_vector()
     origin_x = ( 0.5 - origin[0] ) * 1000.0
     origin_y = ( 0.5 - origin[1] ) * 1000.0
     origin_z = ( 0.5 - origin[2] ) * 1000.0

## This should work as a standalone in reading terrain height elevation data.
## Note: This does not convert spherical,ellipitical, or quasi spherical
## landscape data.  
##TM =[{'Landtype':'Land', 'Type': 'height', 'TBracket':[0,1], 'Fractal': True,
##        'Colors':[[landlow_dirt,0],[landlow,1]], 'Name': 'LLDFractal',
##        'nsize': nsize, 'nbasis': nbasis, 'lacunarity':lacunarity,
##        'depth':depth, 'dimension':dimension, 'id': 1, 'ThreshType': 'height'},
##      {'Landtype':'Land', 'Type': 'height', 'TBracket':[0,1], 'Fractal': True,
##        'Colors':[[landhigh_dirt,0],[landhigh,1]], 'Name': 'LHDFractal',
##        'nsize': nsize, 'nbasis': nbasis, 'lacunarity':lacunarity,
##        'depth':depth, 'dimension':dimension, 'id': 2, 'ThreshType': 'height'},
##     {'Landtype':'Land', 'Type': 'normal', 'TBracket':[.1,1], 'Fractal': True,
##        'Colors':[[landlow_rock,0],[landlow_rock2,1]], 'Name': 'LLRFractal',
##        'nsize': nsize2, 'nbasis': nbasis2, 'lacunarity':lacunarity2,
##        'depth':depth2, 'dimension':dimension2, 'id': 3, 'ThreshType': 'normal'},
##      {'Landtype':'Land', 'Type': 'normal', 'TBracket':[.1,1], 'Fractal': True,
##        'Colors':[[landhigh_rock,0],[landhigh_rock2,1]], 'Name': 'LHRFractal',
##        'nsize': nsize2, 'nbasis': nbasis2, 'lacunarity':lacunarity2,
##        'depth':depth2, 'dimension':dimension2, 'id': 4, 'ThreshType': 'normal'},
##     {'Landtype':'Flood', 'Type': 'height', 'TBracket':[0,1], 'Fractal': True,
##        'Colors':[[waterlow,0],[waterlow2,1]], 'Name': 'WLFractal',
##        'nsize': nsize3, 'nbasis': nbasis3, 'lacunarity':lacunarity3,
##        'depth':depth3, 'dimension':dimension3, 'id': 5, 'ThreshType': 'height'},
##      {'Landtype':'Flood', 'Type': 'height', 'TBracket':[0,1], 'Fractal': True,
##        'Colors':[[waterhigh,0],[waterhigh2,1]], 'Name': 'WHFFractal',
##        'nsize': nsize3, 'nbasis': nbasis3, 'lacunarity':lacunarity3,
##        'depth':depth3, 'dimension':dimension3, 'id': 6, 'ThreshType': 'height'}]

##DCI ={8: waterlow, 9: waterhigh, 15: dark_grass, 16: light_grass,
##      20: rock, 21: dark_rock}
##
##MM = {7: {'id': 7, 'Landtype': 'Flood', 'Ins': (5,6), 'Outs': 7, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'height',
##          'Factor':0, 'Falloff':0},
##      10: {'id': 10, 'Landtype': 'Flood', 'Ins': (8,9), 'Outs': 10, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'normal',
##          'Factor':0, 'Falloff':0},
##      11: {'id': 11, 'Landtype': 'Flood', 'Ins': (7,10), 'Outs': 11, 'Type':,
##          'normal', 'FactorType' : 'fixed', 'FactorVar': 'normal',
##          'Factor':.5, 'Falloff':0},
##      12: {'id': 12, 'Landtype': 'Land', 'Ins': (1,2), 'Outs': 12, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'height',
##          'Factor':0, 'Falloff':0},
##      13: {'id': 13, 'Landtype': 'Land', 'Ins': (15,16), 'Outs': 13, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'normal',
##          'Factor':0, 'Falloff':0},
##      14: {'id': 14, 'Landtype': 'Land', 'Ins': (12,13), 'Outs': 14, 'Type':,
##          'normal', 'FactorType' : 'fixed', 'FactorVar': 'normal',
##          'Factor':.3, 'Falloff':0},
##      17: {'id': 17, 'Landtype': 'Land', 'Ins': (3,4), 'Outs': 17, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'height',
##          'Factor':0, 'Falloff':0},
##      18: {'id': 18, 'Landtype': 'Land', 'Ins': (20,21), 'Outs': 18, 'Type':,
##          'normal', 'FactorType' : 'variable', 'FactorVar': 'normal',
##          'Factor':0, 'Falloff':0},
##      19: {'id': 14, 'Landtype': 'Land', 'Ins': (17,18), 'Outs': 19, 'Type':,
##          'normal', 'FactorType' : 'fixed', 'FactorVar': 'normal',
##          'Factor':.5, 'Falloff':0},
##      22: {'id': 22, 'Landtype': 'Land', 'Ins': (14,19), 'Outs': 22, 'Type':,
##          'normal2', 'FactorType' : 'falloff', 'FactorVar': 'normalT',
##          'Factor':.5, 'Falloff':CFK1},
##      }
##
##CIOM = {}
##
##MD = []
##
##NCs = {5:{'Chain':[7,10,11],'Dependencies':[0]},
##       1:{'Chain':[12,13,14],'Dependencies':[0]},
##       3:{'Chain':[17,18,19],'Dependencies':[1]},
##       19:{'Chain:'[22],'Dependencies':[1,3]}}

def cubicInterpolate(p,x):
	return p[1]+.5*x*(-1.0*p[0]+p[2])+x*x*(p[0]-5.0/2.0*p[1]+2.0*p[2]-.5*p[3])+x*x*x*(-.5*p[0]+1.5*p[1]-1.5*p[2]+.5*p[3])


def bicubicInterpolate(p,x,y):
	arr = []
	for i in range(4):
                v = []
                v.append(p[i][0])
                v.append(p[i][1])
                v.append(p[i][2])
                v.append(p[i][3])
                arr.append(cubicInterpolate(v,y))
        
	return cubicInterpolate(arr, x)

def clamp (val):
	if val > 1.0:
            return 1.0
	elif val < 0.0:
	    return 0.0
	else:
	    return val

def clamp2 (val):
     if val > 1.0:
          return val - int(val)
     elif val < 0.0:
          return abs(val - int(val))
     else:
          return val

def normalize(vec):
    x,y,z = vec
    d = (x*x+y*y+z*z)**.5
    return (x/d,y/d,z/d)

def computeGrad(heightmap, normalmap):
    for i in range(dimX):
        for j in range(dimY):
            if i < dimX-1:
                ival = i+1
            else:
                ival = i
            jval = j
            
            if i == dimX-1:
                ival2 = i-1
            else:
                ival2 = i
            t1 = (ival,jval) in heightmap
            t2 = (ival2,jval) in heightmap
            if not t1 or not t2:
                continue
            sx = heightmap[(ival,jval)] - heightmap[(ival2,jval)]
            if i == 0 or i == dimX-1:
                sx *= 2
            if j < dimY-1:
                jval = j+1
            else:
                jval = j
            ival = i
            
            if j == dimY-1:
                jval2 = j-1
            else:
                jval2 = j
            t1 = (ival,jval) in heightmap
            t2 = (ival,jval2) in heightmap
            if not t1 or not t2:
                    continue
            sy = heightmap[(ival,jval)] - heightmap[(ival,jval2)]
            if j == 0 or j == dimY-1:
                sy *= 2
            vec = (-1.0*NORMFAC*sx, -1.0*NORMFAC*sy, .1)
            vec = normalize(vec)
##            vx,vy,vz = vec
##            vec = (vx/2+.5,vy/2+.5, vz/2+.5)
##            vec = vec/2.0 + .5
            normalmap[(i,j)] = vec
##    double sx = (*heightmap)[terr::Coordpair(x<xzScale-1 ? (double)(x+1) : (double)x, (double)y)] - 
##                        (*heightmap)[terr::Coordpair(x == x0 ? (double)(x-1) : (double)x, (double)y)];
##    if (x == 0 || x == xzScale - 1){ sx *= 2;}
##    double sy = (*heightmap)[terr::Coordpair(x, y < xzScale-1 ? (double)(y+1) : (double)y)] - 
##                        (*heightmap)[terr::Coordpair(x, y == y0 ? (double)(y-1) : (double)y)];
##    if (y == 0 || y == xzScale -1) {sy *= 2;}
##    TPoint3 * vec = new TPoint3(-1.0f*normfac*sx, -1.0f*normfac*sy, 0.1f);
##    //TPoint3 * vec = new TPoint3(sx*yScale, 0.0f, sy*yScale);  //changing -sx, 2*xzScale mid term ??!
##    (*vec) = (*vec).normalize()
            
def addLandmaposition(pos,landmap,landmaprev):
    ##check positions
    ##checking neighboring heightmap pixels assigned to landmap.
    ##It is assumed the first pixel neighbor check means that a unassigned
    ## heightmap pixel has not been assigned, but all checks thereafter do
    ## not have this reliant assumption.  If an assignment has taken place
    ## already then we check to see if landmap assignment is the same
    ## as the checked position if it isn't the we aggregate the data
    ## landmap set of the old and new positions.
    ## if nothing has been assigned then we assign the position a new landmap
    ## identifier.  This builds contiguous landspace assignments, delineating
    ## distinct islands and continents.
    ## landmap identifier 0 is reserved for indexing
    x,y = pos
    ne = (x+1,y+1)
    n = (x,y+1)
    nw = (x-1,y+1)
    w = (x-1,y)
    e = (x+1,y)
    se = (x+1,y-1)
    sw = (x-1,y-1)
    s = (x,y-1)
    assigned = False
    if ne in landmaprev:
        landmaprev[pos] = landmaprev[ne]
        landmap[landmaprev[pos]].append(pos)
        assigned = True
    dset = [n,nw,w,e,se,sw,s]
    for d in dset:
        if d in landmaprev:
            if assigned:
                if landmaprev[d] != landmaprev[pos]:
                    posset = landmap[landmaprev[pos]]
                    posset = posset[0:len(posset)]
                    landmap[landmaprev[d]] += posset
                    del landmap[landmaprev[pos]]
                    for npos in posset:
                        landmaprev[npos] = landmaprev[d]
##                        print(npos)
##                        print(landmaprev[npos])
##                        print(landmaprev[d])
                    
            else:
                landmaprev[pos] = landmaprev[d]
                landmap[landmaprev[pos]].append(pos)
                assigned = True
    if not assigned:
        lident = landmap[0]
        lident += 1
        landmaprev[pos] = lident
        landmap[lident] = [pos]
        landmap[0] = lident
    
    
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
        if c1l[g]>c2l[g]:
            tcolor[g]=c2l[g]+(c1l[g]-c2l[g])*value
        else:
            tcolor[g]=c1l[g]+(c2l[g]-c1l[g])*value
    return tuple(tcolor)

def lerpcolor2(c1, c2, value):
     ## this function does not order function operations on channel weighting
     ## rather is ordered on function operations purely on input ordering
    tcolor = [0,0,0]
    c1l = list(c1)
    c2l = list(c2)
    for g in range(3):
        tcolor[g]=c1l[g]+(c2l[g]-c1l[g])*value
        if  0 > tcolor[g]:
             tcolor[g] = 0
        if tcolor[g] > 255:
             tcolor[g] = 255
    return tuple(tcolor)

def multiply(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          tcolor[g] = c1l[g]*c2l[g]
     return tuple(tcolor)

def screen(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          tcolor[g] = 1-1*(1-c1l[g])*(1-c2l[g])
     return tuple(tcolor)

def overlay(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if c1l[g] < .5:
               tcolor[g] = clamp2(2*c1l[g]*c2l[g])
          else:
               tcolor[g] = clamp2(1-2*(1-c1l[g])*(1-c2l[g]))
     return tuple(tcolor)

def hardlight(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if c2l[g] < .5:
               tcolor[g] = clamp2(2*c1l[g]*c2l[g])
          else:
               tcolor[g] = clamp2(1-2*(1-c1l[g])*(1-c2l[g]))
     return tuple(tcolor)

def softlight(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if c2l[g] < .5:
               tcolor[g] = clamp2(c1l[g] - 1*(.5 - c2l[g])*(.5-1*(.5-c1l[g])(.5-c1l[g])))
          else:
               tcolor[g] = clamp2(c1l[g]+(c2l[g]-.5)*(.5 - 1*(.5-c1l[g])(.5-c1l[g])))
     return tuple(tcolor)

def dodge(c1,c2, mode):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if mode == 'Screen':
               tcolor[g] = 1-1*(1-c1l[g])*(1-c2l[g])
          elif mode == 'ColorDodge':
               if c1l[g] == 1:
                    tcolor[g] = 1
               else:
                    tcolor[g] = clamp2(c2l[g] / (1-c1l[g]))
          elif mode == 'LinearDodge':
               tcolor[g] = clamp2(c1l[g]+c2l[g])
               
     return tuple(tcolor)

def burn(c1,c2, mode):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if mode == 'Multiply':
               tcolor[g] = c1l[g]*c2l[g]
          elif mode == 'ColorBurn':
               if c1l[g] == 0:
                    tcolor[g] = 1
               else:
                    tcolor[g] = clamp2(1 - 1*(1 - c2l[g])/c1l[g])
          elif mode == 'LinearBurn':
               tcolor[g] = clamp2(1-1*(c1l[g]+c2l[g]))
     return tuple(tcolor)

def vividlight(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if c2l[g] > .5:
               if c1l[g] == 1:
                    tcolor[g] = 1
               else:
                    tcolor[g] = clamp2(c2l[g] / (1-c1l[g]))
          else:
               if c1l[g] == 0:
                    tcolor[g] = 1
               else:
                    tcolor[g] = clamp2(1 - 1*(1 - c2l[g])/c1l[g])
     return tuple(tcolor)

def difference(c1, c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          tcolor[g] = clamp2(c2l[g] - c1l[g])
     return tuple(tcolor)

def divide(c1,c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          if c2l[g] == 0:
               tcolor[g] = 1
          else:
               tcolor[g] = clamp2(c1l[g]/c2l[g])
     return tuple(tcolor)

def darkenonly(c1,c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          tcolor[g] = min(c1l[g],c2l[g])
     return tuple(tcolor)

def lightenonly(c1,c2):
     ## assumed color values are normalized rgb channels
     tcolor = [0,0,0]
     c1l = list(c1)
     c2l = list(c2)
     for g in range(3):
          tcolor[g] = max(c1l[g],c2l[g])
     return tuple(tcolor)

def shrtdistance(v, vals):
     valsl = list(vals)
     diff = {}
     mindist = float('inf')
     mindistval = -1
     for val in vals:
          diff = abs(val - v)
          if diff < mindist:
               mindist = diff
               mindistval = val
     return mindistval

def getbounds(v, vals, shortdist):
     ## assumed list ordered
     si = vals.index(shortdist)
     if v < shortdist:
          if (si-1) < 0:
               return [si, si]
          else:
               return [si-1,si]
     else:
          if si+1 > len(vals)-1:
               return [si,si]
          else:
               return [si,si+1]

def rescaletonormalpos(pos1,pos2, v):
     ## assumed pos2 >= v >= pos1
     p1 = 0
     p2 = pos2 - pos1
     nv = v-pos1
     return nv/p2
     
def interpcolorpos(v, colors):
     colorsd = {}
     vals = []
     for color in colors:
          c, pos = color
          colorsd[pos] = c
          vals.append(pos)
     vals.sort()
     mindist = shrtdistance(v, vals)
     bounds = getbounds(v,vals, mindist)
     b1, b2 = bounds
     p1 = vals[b1]
     p2 = vals[b2]
     if b1 == b2:
          return colordsd[p1]
     else:
          ## color interpolation is defined where 2 colors are normalized
          ## on a distance range of 1.  So we need to translate and rescale
          ## v to find its interpolated color.  That is, we need to construct
          ## the proper coordinate system for properly linearly interpolating
          ## colors that aren't readily set with one color at origin 0 and
          ## the other at position 1.
          return lerpcolor2(colors[p1],colors[p2],
                            rescaletonormalpos(p1,p2,v))

def getCubicY(cfs, x):
     return cfs[0]*x*x*x + cfs[1]*x*x+cfs[2]*x+cfs[3]

def checksetNorm(minnormz,maxnormz,NORM):
     if minnormz < 0 and maxnormz < 0:
          NORM = 0
     else:
          NORM = 1

def getNormcutoff(NORM, normdiff, minormz, maxnormz, cscale):
     if NORM:
          return maxnormz - cscale*normdiff
     else:
          return minnormz + cscale*normdiff

def getpixel(uvpixcoord ,dimX = dimX, dimY = dimY):
    px,py = uvpixcoord
##    px = ux*dimX
##    py = uy*dimY
    pyi = py*dimX*4
    pxi = px*4
    pix = pyi + pxi
    return (pix,pix+1,pix+2,pix+3)

def getpixelcoord(co, trf, scf):
    ## requires trf 2dimension translation factor
    ## requires scf 2dimension scale factor 
    cox,coy = co
    trfx,trfy = trf
    scfx,scfy = scf
    tcox = cox - trfx
    tcoy = coy - trfy
    return [tcox*scfx, tcoy*scfy]

def translatecoords(heights, trns):
    for index, height in enumerate(heights):
        heights[index] = [height[0] - trns[0],height[1] - trns[1],height[2]]
    return heights




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
## color values are assigned in (r,g,b,a) 8-bit channel format
## or 32 bits RGBA alpha where each channel has 256 integer value ranges

## Iterate the faces to fill the pixel area
scn = bpy.context.scene
## Landscape assumed selected
ob = scn.objects.active
##ob.select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bm = bmesh.from_edit_mesh(ob.data)
D = bpy.data
 
# BlendDataImages.new(name, width, height, alpha=False, float_buffer=False)
##image_object = D.images.new("new",dimX, dimY)
heights = {}
heightmap2 = {}
normalmap = {}
pixheightmap = {}
maxpxx = 0
maxpxy = 0

## assumed Square landscape otherwise dimensions will need to be specified
## in terms of length and width of faces

fdim = len(bm.faces)/2
vdim = len(bm.verts)**.5
Scalefx = dimX / vdim ## scale factor x dimension
Scalefy = dimY / vdim ## scale factor y dimension
## fail safe approach neither assumes ordering on indexing when rescaling
## vertice.
## To iterate vertices and determine min max on xy range
maxvi = 0
minvi = 0
maxvcox = -1*float('inf')
maxvcoy = -1*float('inf')
hmax = -1*float('inf')
minvcox = float('inf')
minvcoy = float('inf')
hmin = float('inf')
maxnormz = -1*float('inf')
minnormz = float('inf')
##maxvcox, maxvcoy,hmax = bm.verts[maxvi].co
##minvcox,minvcoy,hmin  = bm.verts[minvi].co
maxvhi = 0
minvhi = 0
for v in bm.verts:
    x,y,h = v.co
    nz = v.normal[2]
    if x < minvcox and y < minvcoy:
        minvi = v.index
        minvcox = x
        minvcoy = y
    if x > maxvcox and y > maxvcoy:
        maxvi = v.index
        maxvcox = x
        maxvcoy = y
    if h > hmax:
        maxvhi = v.index
        hmax = h
    if h < hmin:
        minvhi = v.index
        hmin = h
    if nz > maxnormz:
        maxnormz = nz
    if nz < minnormz:
        minnormz = nz
        
trfacx = minvcox
trfacy = minvcoy
Scalefx = dimX/abs(maxvcox - minvcox)
Scalefy = dimY/abs(maxvcoy - minvcoy)
trf = [trfacx,trfacy]
scf = [Scalefx,Scalefy]
normdiff = abs(maxnormz - minnormz)
cscale = .1


     
if minnormz < 0 and maxnormz < 0:
     normcutoff = minnormz + cscale*normdiff  ## you can increase or decrease 2nd term to change width of rock banding
     NORM = 0
else:
     normcutoff = maxnormz - cscale*normdiff
     NORM = 1
diff = abs(hmax-hmin)
flood=0.01  ## flood plain
mount=0.50 ##mountain level
	
flood*=diff
mount*=diff
flood+=hmin
mount+=hmin

landmap = {}
landmaprev = {}
landmap[0] = 1

for f in bm.faces:
    nverts = []
    vertmatch = False
    for l in f.verts:
        ## get vert index boundaries
        if l.index in nverts:
            vertmatch = True
            break
        nverts.append(l.index)    
    ## get uv coord
    if vertmatch:
        continue
    coords = []
    heights = []
    normals = []
    for vi,nvert in enumerate(nverts):
##        vcoord = vcoordtovindexrev[vi]
##        uvcoord = sphereproj[vcoord]
##        print(vi)
        coord = f.verts[vi].co[0:2]
        height = f.verts[vi].co[2]
        normal = f.verts[vi].normal[2]
        pxc,pyc = getpixelcoord(coord, trf, scf)
        coords.append(list(coord))
        heights.append([pxc,pyc,height])
        normals.append([pxc,pyc,normal])
        pixheightmap[(pxc,pyc)] = height
        if pxc > maxpxx:
                maxpxx = pxc
        if pyc > maxpxy:
                maxpxy = pyc
    ## get min max coords
    sortset = coords[0:len(coords)]
    sortset.sort(key=lambda tup: tup[0])
    minset = sortset[0:2]
    maxset = sortset[2:4]
    minset.sort(key=lambda tup:tup[1])
    maxset.sort(key=lambda tup:tup[1])
    mincoord = minset[0]
    maxcoord = maxset[1]
    ## now we convert min max coords to pixel coordinates
    minpixcoord = getpixelcoord(mincoord,trf,scf)
    maxpixcoord = getpixelcoord(maxcoord,trf,scf)
    ## to use a translation shift factor ans so scale so that we can properly
    ## compute heighmap values
##    minx,miny = minpixcoord
##    maxx,maxy = maxpixcoord
##    trnsx = minx - int(minx)
##    trnsy = miny - int(miny)
##    trns = (trnsx,trnsy)
##    uvheights = translatecoords(uvheights, trns)
##    minpixcoord = (minx-transx, miny-transy)
##    maxpixcoord = (maxx-transx, maxy-transy)
##    ## now compute scale factor from maxcoord
##    if int(maxy) != int(maxpixcoord[1]):
        
    ## now we iterate the set of pixels from minpix x to maxpix along x
    ## and minpix y to maxpix y
    pixcoord = minpixcoord
    startx = None
    starty = None
    difx = minpixcoord[0] - int(minpixcoord[0])
    if difx == 0.0:
        startx = int(minpixcoord[0])
    else:
        startx = int(minpixcoord[0])+1
    dify = minpixcoord[1] - int(minpixcoord[1])
    if dify == 0.0:
        starty = int(minpixcoord[1])
    else:
        starty = int(minpixcoord[1])+1
    for j in range(starty,int(maxpixcoord[1])+1):
        for i in range(startx,int(maxpixcoord[0])+1):
##            print(float(i))
##            print(float(j))
##            print(uvheights)
            if not BICUBIC:
                h = bilinear_interpolation(float(i),
                                           float(j), heights) ## bilinearly interpolated height for uv
                h += -1*hmin
                heightmap2[(i,j)] = h
                normalmap[(i,j)] = bilinear_interpolation(float(i),
                                                          float(j),
                                                          normals)
            else:
                print("Not there yet!")
##                x = i 
##                y = j	
####                ///*		 
####                //int p0x = ((x == size ? (int)x - 1 : (int)x); int p0y = ((y == size ? (int)y - 1 : (int)y);
##                p1x = x
##                p1y = y
##                locx = x -p1x; double locy = y-p1y;
####                //int p1x = ((x == size ? (int)x : (int)x + 1); int p1y = ((y == size ? (int)y : (int)y + 1); 
##                p2x = x+1
##                p2y = y+1
##                if x <= 0:
##                        p0x = p1x
##                else:
##                        p0x = p1x-1
##                if y <= 0:
##                        p0y = p1y
##                else:
##                        p0y = p1y-1
##                ##p0x = (x <= 0 ? p1x : p1x-1); int p0y = (y <= 0 ? p1y : p1y-1);
##                if x >= dimX:
##                        p3x = p2x
##                else:
##                        p3x = p2x+1
##                if y >= dimY:
##                        p3y = p2y
##                else:
##                        p3y = p2y+1
####                int p3x = (x >= (size-2.0f) ? p2x : p2x+1); int p3y = (y >= (size-2.0f) ? p2y : p2y+1);
##                p00 = (p0x,p0y); p01 = (p0x,p1y); p02 = (p0x,p2y); p03 = (p0x,p3y);
##		p10 = (p1x,p0y); p11 = (p1x,p1y); p12 = (p1x,p2y); p13 = (p1x,p3y);
##                p20 = (p2x,p0y); p21 = (p2x,p1y); p22 = (p2x,p2y); p23 = (p2x,p3y);
##                p30 = (p3x,p0y); p31 = (p3x,p1y); p32 = (p3x,p2y); p33 = (p3x,p3y);
##                a = [[],[],[],[]]
##                t1 = p00 in heightmap; t2 = p01 in heightmap; t3 = p02 in heightmap;
##                t4 = p03 in heightmap; t5 = p10 in heightmap; t6 = p11 in heightmap;
##                t7 = p12 in heightmap; t8 = p13 in heightmap; t9 = p20 in heightmap;
##                t10 = p21 in heightmap; t11 = p22 in heightmap; t12 = p23 in heightmap;
##                t13 = p30 in heightmap; t14 = p31 in heightmap; t15 = p32 in heightmap;
##                t16 = p33 in heightmap;
##                t17 = not t1 or not t2 or not t3 or not t4 or not t5 or not t6 or not t7 or not t8
##                t18 = not t9 or not t10 or not t11 or not t12 or not t13 or not t14 or not t15 or not t16
##                if t17 or t18:
##                        continue
##                else:
##			a[0][0] = heightmap2[p00]; a[0][1] = heightmap[p01]; 
##			a[0][2] = heightmap2[(*p02)]; a[0][3] = (*heightmap)[(*p03)]; 
##			a[1][0] = (*heightmap)[(*p10)]; a[1][1] = (*heightmap)[(*p11)]; 
##			a[1][2] = (*heightmap)[(*p12)]; a[1][3] = (*heightmap)[(*p13)];
##			a[2][0] = (*heightmap)[(*p20)]; a[2][1] = (*heightmap)[(*p21)]; 
##			a[2][2] = (*heightmap)[(*p22)]; a[2][3] = (*heightmap)[(*p23)];
##			a[3][0] = (*heightmap)[(*p30)]; a[3][1] = (*heightmap)[(*p31)]; 
##			a[3][2] = (*heightmap)[(*p32)]; a[3][3] = (*heightmap)[(*p33)];                        
##computeGrad(heightmap2, normalmap)
gval5 = 0
for j in range(dimY):
    for i in range(dimX):
        if not (i,j) in normalmap:
                continue
##        x,y,z = normalmap[(i,j)]
        z = normalmap[(i,j)]
        if not (i,j) in heightmap2:
                continue
        h = heightmap2[(i,j)]
        dw = (1.0-(z*z))**.5 ## //normals weighting when normal is positive z then 0 normal weight
        dw = clamp(dw)            
        if (h<flood):
            ncoords3 = (i /nsize3 + origin_x, j/ nsize3 + origin_y,
                        0.0 + origin_z)
            gval6 = fractal(ncoords3,dimension3,lacunarity3,depth3,nbasis3)
            gval6 += 1
            gval6 *= .5
            gval6 = clamp(gval6)
            newcolorl = lerpcolor(waterlow,waterlow2,gval6)
            newcolorh = lerpcolor(waterhigh,waterhigh2,gval6)
            newcolor=lerpcolor(newcolorl,newcolorh,h/flood)

            newcolor2 = lerpcolor(waterlow,waterhigh,dw)
            newcolor = lerpcolor(newcolor,newcolor2,.5)
        elif (h>mount):
            newcolor=lerpcolor(mountlow,mounthigh,(h-mount)/(hmax-mount))
            addLandmaposition((i,j),landmap,landmaprev)
            newcolor2 = lerpcolor(mountlow,mounthigh,(z-minnormz)/(normdiff))
            newcolor = lerpcolor(newcolor,newcolor2,.5)                
        else:
            ncoords = ( i / nsize + origin_x, j / nsize+origin_y,
                        0.0 + origin_z )
            ncoords2 = (i /nsize2 + origin_x, j/ nsize2 + origin_y,
                        0.0 + origin_z)

            gval = fractal(ncoords, dimension, lacunarity, depth, nbasis )
            gval2 = fractal(ncoords2,dimension2,lacunarity2,depth2,nbasis2)

            ## gval gradient value is returned from -1 to 1
            ## need to shift and rescale to 0 to 1
            gval += 1
            gval *= .5
            gval2 += 1
            gval2 *= .5

##            if random.random() > .5:
            landlow_n = lerpcolor(landlow_dirt,landlow,gval)
            landhigh_n = lerpcolor(landhigh_dirt,landhigh,gval)
            newcolor = lerpcolor(landlow_n,landhigh_n,
                                 (h-flood)/(mount-flood))
##                newcolor = lerpcolor(landlow_dirt,landhigh_dirt,
##                                     (h-flood)/(mount-flood))
##            else:
##                newcolor=lerpcolor(landlow,landhigh,(h-flood)/(mount-flood))
            addLandmaposition((i,j),landmap,landmaprev)
##            newcolor2 = lerpcolor(landlow,landhigh,dw)
            newcolor2 = lerpcolor(dark_grass,light_grass,
                                  (z-minnormz)/(normdiff))
            newcolor = lerpcolor(newcolor,newcolor2,.3)
            if NORM:
                 testc = z <= normcutoff
                 ratioc = abs((z-minnormz)/(minnormz - normcutoff))
                 rncdiff = abs((z-normcutoff)/(minnormz - normcutoff))
            else:
                 testc = z >= normcutoff
                 ratioc = abs((maxnormz-z)/(maxnormz-normcutoff))
                 rncdiff = abs((z-normcutoff)/(maxnormz-normcutoff))
            if testc:
                    landlow_rockn = lerpcolor(landlow_rock,landlow_rock2,gval2)
                    landhigh_rockn = lerpcolor(landhigh_rock,landhigh_rock2,
                                               gval2)
                    newcolor3 = lerpcolor(landlow_rockn,landhigh_rockn,
                                         (h-flood)/(mount-flood))
##                    newcolor = lerpcolor(landlow_rock,landhigh_rock,
##                                         (h-flood)/(mount-flood))
                    newcolor4 = lerpcolor(rock,dark_rock,ratioc)
                    newcolor5 = lerpcolor(newcolor3,newcolor4,.5)
                    ## feathering color
##                    ncdiff = abs((z-normcutoff)/(maxnormz-normcutoff))
                    if rncdiff < 0:
                            print(rncdiff)
                    ## using 3rd degree polynomial for falloff
                    ## -83.3021 x^3-72.8482 x^2+18.1178 x
                    ## use cf for reference polys it is keyed from .1 to .7
                    if rncdiff > CFK1:
                            gval3 = 1
                    else:
                            gval3 = cf[CFK1][0]*rncdiff*rncdiff*rncdiff +cf[CFK1][1]*rncdiff*rncdiff+cf[CFK1][2]*rncdiff + cf[CFK1][3]
                    newcolor = lerpcolor2(newcolor,newcolor5,gval3)
##                    newcolor = newcolor5
            hth = abs((h-mount)/(hmax-mount))
            if hth <= .1:
                    newcolor6=lerpcolor(mountlow,mounthigh,abs((h-mount)/(hmax-mount)))
                    newcolor7 = lerpcolor(mountlow,mounthigh,(z-minnormz)/(normdiff))
                    newcolor8 = lerpcolor(newcolor6,newcolor7,.5)
                    gval4 = -83.3021*hth*hth*hth - 72.8482*hth*hth+18.1178*hth
                    newcolor = lerpcolor2(newcolor,newcolor8,1-gval4)
            hfth = abs((h-flood)/(hmin-flood))
            if hfth <= .1:
##                    newcolor9=lerpcolor(mountlow,mounthigh,abs((h-mount)/(hmax-mount)))
##                    newcolor10 = lerpcolor(mountlow,mounthigh,(z-minnormz)/(normdiff))
##                    newcolor11 = lerpcolor(newcolor9,newcolor10,.5)

                    ncoords3 = (i /nsize3 + origin_x, j/ nsize3 + origin_y,
                                0.0 + origin_z)
                    gval6 = fractal(ncoords3,dimension3,lacunarity3,depth3,nbasis3)
                    gval6 += 1
                    gval6 *= .5
                    gval6 = clamp(gval6)
                    newcolorl = lerpcolor(waterlow,waterlow2,gval6)
                    newcolorh = lerpcolor(waterhigh,waterhigh2,gval6)
                    newcolor9 = lerpcolor(newcolorl,newcolorh,h/flood)

                    newcolor10 = lerpcolor(waterlow,waterhigh,dw)
                    newcolorw = lerpcolor(newcolor9,newcolor10,.5)
                    gval5 = -83.3021*hfth*hfth*hfth - 72.8482*hfth*hfth+18.1178*hfth
                    newcolor = lerpcolor2(newcolor,newcolorw,1-gval5)
##                    newcolor = lerpcolor(dark_rock,rock,(h-flood)/(mount-flood))
        ## assign the newcolor to the blender image pixel indices per channel
        r,g,b = newcolor
        
        ##rchi,gchi,bchi,achi = getpixel((i,j))
        if not (0<= r < 256):
                print('r out of bounds')
                print(r)
                print(gval5)
                print(ncoords3)
                print(h/flood)
                print(dw)
                if h < flood:
                        print('h is a flood coordinate')
        if not (0<= g < 256):
                print('g out of bounds')
                print(g)
                if h < flood:
                        print('h is a flood coordinate')
        if not (0<= b < 256):
                print('b out of bounds')
                print(b)
                if h < flood:
                        print('h is a flood coordinate')
        colormap[(i,j)] = (r,g,b)
##            image_object.pixels[rchi] = (r/255.0)
##            image_object.pixels[gchi] = (g/255.0)
##            image_object.pixels[bchi] = (b/255.0)
##            image_object.pixels[achi] = (1.0)
            ## that should be it!
filename = "/home/strangequark/colormap.txt"
out = open(filename, 'w')
out.write(str(colormap))
out.close()
##for cont in landmap:
##    if cont != 0:
##        print('Area of ', cont, ' equals: ', len(landmap[cont]))
