import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import r
from unionfind import UnionFind



def define_shells_structure(me):
    union_find = UnionFind(len(me.vertices))
    [union_find.unify(v1, v2) for v1, v2 in [(edge.vertices) for edge in me.edges]]

    return union_find
    

def get_num_shells(me, debug=True):
    union_find = define_shells_structure(me)
    
    if (debug):
        print("Number of shells: " + str(union_find.components()))

    return union_find.components()


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
    print("\n--------------- Ex 6. SHELLS -----------------")
    get_num_shells(mesh)
    print("-------------------------------------------------")        

    

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


if __name__ == "__main__":
   main()