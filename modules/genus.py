import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r
from shells import get_num_shells



def get_genus(me, debug=True):

    # Euler-Poincaré equation: F + V = E + R + 2(S - H).
    # Then, H = (E + R - F - V)/2 + S.
    # Blender does not include rings, hence:
    # H = (E - F - V)/2 + S
    num_genus = int((len(me.edges) - len(me.polygons) - len(me.vertices)) / 2) + get_num_shells(me)

    if (debug):
        print("Number of genus: " + str(num_genus)) 

    return num_genus    


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
    print("\n--------------- GENUS -----------------")
    get_genus(mesh)
    print("-------------------------------------------------") 

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


# main()
