## Spherical subdivision
import math
import bpy,bmesh
import random
## spherical coordinates
anglesub = 100
Radius  = .02
Iterations = 2000
Height = .00001

def distance(coord):
    x,y,z = coord
    return (x*x+y*y+z*z)**.5

def dotproduct(c1,c2):
    x1,y1,z1 = c1
    x2,y2,z2 = c2
    return x1*x2+y1*y2+z1*z2

def norm(coord):
    d = distance(coord)
    x,y,z = coord
    return (x/d,y/d,z/d)

def addvec(v1,v2):
    x1,y1,z1 = v1
    x2,y2,z2 = v2
    return (x1+x2,y1+y2,z1+z2)

def scalemult(sc,v1):
    x1,y1,z1 = v1
    return (sc*x1,sc*y1,sc*z1)

def spheretocoord(r,theta,phi):
    return (r*math.cos(theta)*math.sin(phi), r*math.sin(theta)*math.sin(phi),
            r*math.cos(phi))

def randomNormal():
    theta = random.uniform(0.0,2*math.pi)
    phi = random.uniform(0.0,2*math.pi)
    return spheretocoord(1.0,theta,phi)

def buildSphere(Radius, anglesub):
    ## build equitorial subdivision
    pi2 = 2*math.pi
    pi = math.pi
    sphereproj = {}
    thetainc = 2*math.pi/anglesub
    vertices = []
    theta = 0.0
    phi = math.pi/2.0
    for i in range(anglesub+1):
        v = spheretocoord(Radius,theta,phi)
        vertices.append(v)
        sphereproj[v] = (theta/pi2,phi/pi)
        theta += thetainc
    ## now build positive hemisphere
    evertices = vertices[0:len(vertices)]
    theta = 0.0
    phi -= thetainc
    vertgroups = []
    ##vertgroups += [vertices]
    for i in range(int(anglesub/4+1)):
        theta = 0.0
        verts = []  ## we build a ordered list as we increment phi of vertices
        if i != int(anglesub/4 ):
            for j in range(anglesub+1):
                v = spheretocoord(Radius,theta,phi)
                verts.append(v)
                sphereproj[v] = (theta/pi2,phi/pi)
                theta += thetainc
            phi -= thetainc
            vertgroups.append(verts)
        else:
            v = spheretocoord(Radius,theta,0.0)
            verts.append(v)
            sphereproj[v] = (theta,0.0)
    ## build the faces and append the vertices
    faces = []
    vcoordtovindex = {}
    for i,vert in enumerate(vertices):
        vcoordtovindex[vert] = i
        
    for verts in vertgroups:
        for vert in verts:
            vertices.append(vert)
            vcoordtovindex[vert] = len(vertices)-1
    newvertgroups = [evertices]
    newvertgroups += vertgroups
    vertgroups = newvertgroups
    ##vertgroups += [vertices]
    ifacerow = 0 ## initial face row tracking
    for vgindex,verts in enumerate(vertgroups):
        
        if vgindex == len(vertgroups) -1:
            break
        nvertices = vertgroups[vgindex+1]
        for vindex, vertex in enumerate(verts):
            face = []
            if vindex == len(verts)-1:
                nvindex = 0
            else:
                nvindex1 = vindex+1
            if vgindex+1 == len(vertgroups)-1:
                nv1 = verts[nvindex1]
                nv2 = nvertices[0]
                nv3 = nvertices[0]
            else:
                nv1 = verts[nvindex1]
                nv2 = nvertices[nvindex1]
                nv3 = nvertices[vindex]
            vi = vcoordtovindex[vertex]
            nv1i = vcoordtovindex[nv1]
            nv2i = vcoordtovindex[nv2]
            nv3i = vcoordtovindex[nv3]
            face = (vi,nv1i,nv2i,nv3i)
            if vgindex == 0:
                ifacerow += 1
            faces.append(face)
            ##print(face)
    fvinc = len(vertices)
    ## build negative hemisphere
    theta = 0.0
    phi = math.pi/2.0
    phi += thetainc
    vertgroups = []
    vertgroups += [evertices]
    for i in range(int(anglesub/4+1)):
        theta = 0.0
        verts = []  ## we build a ordered list as we increment phi of vertices
        if i != int(anglesub/4):
            for j in range(anglesub+1):
                v = spheretocoord(Radius,theta,phi)
                verts.append(v)
                vertices.append(v)
                sphereproj[v] = (theta/pi2,phi/pi)
                vcoordtovindex[v] = len(vertices)-1
                theta += thetainc
            phi += thetainc
##            print(phi)
##            vertices += verts[0:len(verts)]
            vertgroups += [verts]
        else:
            ##verts.append(spheretocoord(Radius,theta,phi))
            v = spheretocoord(Radius,theta,pi)
            vertices += [v]
            sphereproj[v] = (theta/pi2,pi/pi)
            vcoordtovindex[v] = len(vertices)-1
            vertgroups += [[v]]
##    newfaces = []
##    for fi, face in enumerate(faces):
##        newface = []
##        if fi <= ifacerow:
##            v1,v2,v3,v4 = face
##            nv1 = v1
##            nv2 = v2
##            nv3 = v3 + fvinc
##            nv4 = v4 + fvinc
##        else:
##            nv1 = v1 + fvinc
##            nv2 = v2 + fvinc
##            nv3 = v3 + fvinc
##            nv4 = v4 + fvinc
##        newface = (nv1,nv2,nv3,nv4)
##        newfaces.append(newface)
##    faces += newfaces
    for vgindex,verts in enumerate(vertgroups):
        
        if vgindex == len(vertgroups) -1:
            break
        nvertices = vertgroups[vgindex+1]
        for vindex, vertex in enumerate(verts):
            face = []
            if vindex == len(verts)-1:
                nvindex = 0
            else:
                nvindex1 = vindex+1
            if vgindex+1 == len(vertgroups)-1:
                nv1 = verts[nvindex1]
                nv2 = nvertices[0]
                nv3 = nvertices[0]
            else:
                nv1 = verts[nvindex1]
                nv2 = nvertices[nvindex1]
                nv3 = nvertices[vindex]
            vi = vcoordtovindex[vertex]
            nv1i = vcoordtovindex[nv1]
            nv2i = vcoordtovindex[nv2]
            nv3i = vcoordtovindex[nv3]
            ##face = (vi,nv1i,nv2i,nv3i)
            face = (vi,nv3i,nv2i,nv1i)
            if vgindex == 0:
                ifacerow += 1
            faces.append(face)
    
    return vertices, faces, sphereproj, vcoordtovindex

                
vertices, faces, sphereproj, vcoordtovindex = buildSphere(Radius, anglesub)
heightmap = {} ## vertex index keyed, heightmap valued
i = 0
while i < Iterations:
    rN = randomNormal()
    height = Height*random.random()
    for vi, vert in enumerate(vertices):
        vN = norm(vert)
        if dotproduct(rN,vN) > 0:
            vheight = scalemult(height,vN)
            newvec = addvec(vert,vheight)
        else:
            vheight = scalemult(-1*height,vN)
            newvec = addvec(vert,vheight)
        heightmap[vi] = height
        del vcoordtovindex[vert]
        scoord = sphereproj[vert]
        sphereproj[newvec] = scoord
        del sphereproj[vert]
        vcoordtovindex[newvec] = vi
        vertices[vi] = newvec
    i += 1

## setreverse index mapping between coordinate to indices
vcoordtovindexrev = {}
for vcoord in vcoordtovindex:
    vi = vcoordtovindex[vcoord]
    vcoordtovindexrev[vi] = vcoord
    
meshName = "Polygon"
obName = "PolygonObj"
me = bpy.data.meshes.new(meshName)
ob = bpy.data.objects.new(obName, me)
ob.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(ob)
me.from_pydata(vertices,[],faces)      
me.update(calc_edges=True)
## Select the new object in scene and set uvs
scn = bpy.context.scene
scn.objects.active = ob
ob.select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bm = bmesh.from_edit_mesh(ob.data)
uv_layer = bm.loops.layers.uv.verify()
bm.faces.layers.tex.verify()

for f in bm.faces:
    for l in f.loops:
        luv = l[uv_layer]
        vind = l.vert.index
        vcoord = vcoordtovindexrev[vind]
        uvcoord = sphereproj[vcoord]
        luv.uv = tuple(uvcoord)

bmesh.update_edit_mesh(me)
bpy.ops.object.mode_set(mode='OBJECT')
