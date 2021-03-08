import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from utils import r

def get_centroid(me):

    centroid = mathutils.Vector([0,0,0])
    for i in range(len(me.vertices)):
        centroid = centroid + (me.vertices[i].co / float(len(me.vertices)))
        
    return centroid


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
    centroid = [r(get_centroid(mesh)[i]) for i in range(3)]
    print("Centroid: " + str(centroid))

    # Report performance...
    print("Script took %6.2f secs.\n\n"%(time()-t))


main()