import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r
from area import get_polygon_area


def get_volume(me, debug=True):

    total_volume = 0

    for polygon in me.polygons:
        
        area_polygon = get_polygon_area(me, polygon, False)
        
        # To compute the volume, we will add the signed volume that every polygon forms with the origin
        # Each volume will be a pyramid with an already known base:
        # Face volume = 1/3 * b * h --> b: base area (known), h: pyramid height (to compute)
        # In this case, height computation is a point to plane distace problem which can be solved
        # with a single dot product h = v · n --> v = P-Q --> P: Origin, Q: Point in plane, n: face normal
        
        # v = P - Q = O - arbitrary vertex in polygon
        v = -me.vertices[polygon.vertices[0]].co
        h = v.dot(polygon.normal)

        face_volume = 1/3 * area_polygon * h
        total_volume += face_volume/2

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
    print("\n--------------- Ex 9. VOLUME -----------------")
    get_volume(mesh)
    print("-------------------------------------------------") 

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


main()
