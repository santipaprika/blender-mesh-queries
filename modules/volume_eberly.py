import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r
from area import get_polygon_area
from manifolds import get_non_manifold_shells


# Volume computation based on:
# Eberly, D. (2003). Polyhedral mass properties (revisited). 
# https://www.cs.upc.edu/~virtual/SGI/docs/3.%20Further%20Reading/Polyhedral%20Mass%20Properties%20Revisited.pdf.

def get_volume(me, debug=True):

    total_volume = 0
    M = [[5,5,5],[11,2,2],[2,11,2],[2,2,11]]
    W = [-27/96., 25/96., 25/96., 25/96.]

    # get non-manifold shells
    non_manifold_shells, union_find = get_non_manifold_shells(me)

    for polygon in me.polygons:
        
        # find if polygon belongs to a connected component by checking the shell of a vertex of the polygon
        # find takes amortized constant time because of union find path compression
        if union_find.find(polygon.vertices[0]) in non_manifold_shells:
            continue

        n = len(polygon.vertices)
        V = [me.vertices[polygon.vertices[i]] for i in range(n)]

        i=0
        j=1
        for k in range(2,n):
            nx,ny,nz = (V[j].co-V[i].co).cross(V[k].co-V[j].co)

            for p in range(4):
                x,y,z = (M[p][0]*V[i].co + M[p][1]*V[j].co + M[p][2]*V[k].co) / 15.
                total_volume += W[p] * (x*nx + y*ny + z*nz)/3.

            j=k
        

    if (debug):
        print("Total volume: " + str(r(abs(total_volume))))


def main(): 
    # Retrieve the active object (the last one selected)
    ob = bpy.context.active_object

    # Check that it is indeed a mesh
    if not ob or ob.type != 'MESH': 
        print("Active object is not a MESH! Aborting...")
        return
           
    # If we are in edit mode, return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Retrieve the mesh data
    mesh = ob.data  
    
    # Get current time
    t = time()

    # Function that does all the work
    print("\n--------------- VOLUME -----------------")
    get_volume(mesh)
    print("-------------------------------------------------") 

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


# main()
