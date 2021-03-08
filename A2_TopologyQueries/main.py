import bpy 
from time import time
import centroid

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
    centroid = centroid.get_centroid(mesh)
    print("Centroid: " + str(centroid))

    # Report performance...
    print("Script took %6.2f secs.\n\n"%(time()-t))


main()