import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r

def get_manifolds(me):

    edge_polygons = {}

    for polygon in me.polygons:
        for edge_key in polygon.edge_keys:
            edge_polygons[edge_key] = [polygon.index] if edge_key not in edge_polygons else edge_polygons[edge_key] + [polygon.index]

    #boundary_edges, boundary_edges_faces = [] for i in range(2)
    # boundary_edges, boundary_edges_faces = [edge_key] 
    boundary = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) == 1}
    manifolds = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) == 2}
    non_manifolds = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) > 2}

    # boundary = dict(zip((i,k) for i,k in edge_polygons.items() if len(edge_polygons[i]) == 1))
    # manifolds = dict(zip((i,k) for i,k in edge_polygons.items() if len(edge_polygons[i]) == 2))
    # non_manifolds = dict(zip((i,k) for i,k in edge_polygons.items() if len(edge_polygons[i]) > 2))
    #manifolds = [i for i in edge_polygons if len(edge_polygons[i]) == 2]
    #non_manifolds = [i for i in edge_polygons if len(edge_polygons[i]) > 2]
    
    print("\n--------------- Ex 4. MANIFOLDS -----------------")
    print("Boundary edges: " + str(len(boundary)))
    print("Manifold edges: " + str(len(manifolds)))
    print("Non Manifold edges: " + str(len(non_manifolds)))
    print("-------------------------------------------------")

    return manifolds


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
    get_manifolds(mesh)

    # Report performance...
    print("Script took %6.2f secs.\n\n"%(time()-t))
