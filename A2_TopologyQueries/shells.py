import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r
from unionfind import UnionFind



def get_shells(me):
    union_find = UnionFind(len(me.vertices))
    [union_find.unify(v1, v2) for v1, v2 in [(edge.vertices) for edge in me.edges]]

    # for edge in me.edges:
        # [union_find.unify(v1, v2) for v1,v2 in [edge.vertices]]
            

    print(union_find.components())



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
    get_shells(mesh)

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


main()
