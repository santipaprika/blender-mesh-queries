import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import r
from shells import define_shells_structure


# get non manifold / bounded shells
def get_non_manifold_shells(me):
    non_man_edge_keys = get_non_manifold_edges(me)
    non_man_vertices = set([non_man_edge_keys[i][j] for j in range(2) for i in range(len(non_man_edge_keys))])

    union_find = define_shells_structure(me)

    # define as set to avoid repetitions
    non_man_shells = set()

    # store the indices of the non-manifold/bounded shells
    for vtx in non_man_vertices:
        # find takes constant time
        non_man_shells.add(union_find.find(vtx))

    return non_man_shells, union_find


# get non manifold / boundary edges
def get_non_manifold_edges(me):
    edge_polygons = {}

    for polygon in me.polygons:
        for edge_key in polygon.edge_keys:
            edge_polygons[edge_key] = [polygon.index] if edge_key not in edge_polygons else edge_polygons[edge_key] + [polygon.index]

    non_manifolds = [edge_key for edge_key in edge_polygons.keys() if len(edge_polygons[edge_key]) != 2]

    return non_manifolds


def get_manifolds(me):

    edge_polygons = {}

    for polygon in me.polygons:
        for edge_key in polygon.edge_keys:
            edge_polygons[edge_key] = [polygon.index] if edge_key not in edge_polygons else edge_polygons[edge_key] + [polygon.index]

    boundary = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) == 1}
    manifolds = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) == 2}
    non_manifolds = {edge_key:faces for edge_key, faces in edge_polygons.items() if len(edge_polygons[edge_key]) > 2}

    print("\n---------------- MANIFOLDS ------------------")
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


if __name__ == "__main__":
   main()