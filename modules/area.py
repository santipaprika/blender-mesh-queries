import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import r

def get_polygon_area(me, polygon, debug=True):
    # Get polygon vertices
    vidx = polygon.vertices
    len_vertices = len(vidx)

    # Add up signed area of every triangle joining the origin and two consecutive vertices:
    # Area_OAB = 1/2 * (OA x OB), where A and B are consecutive vertices. 
    # iterating for all triangles (compatible with concave polygons as well):
    # Area = 1/2 * sum for all i < len(V) of (v_i X v_(i+1))
    cross_comps = [me.vertices[vidx[i]].co.cross(me.vertices[vidx[(i+1) % len_vertices]].co) for i in range(len_vertices)]
    area_polygon = mathutils.Vector()
    for i in range(len_vertices):
        area_polygon += cross_comps[i]
    
    if debug:
        print("Polygon area (own method): " + str(r(area_polygon.length/2)))
        print("Polygon area (blender attribute): " + str(r(polygon.area)))

    return area_polygon.length

def get_area(me, debug=True):

    total_area = 0
    total_blender = 0

    for polygon in me.polygons:
        
        area_polygon = get_polygon_area(me, polygon, debug)
        
        total_area += area_polygon/2
        total_blender += polygon.area

    if debug:
        print("************************************")
        print("Total surface area (own method): " + str(r(total_area)))
        print("Total surface area (blender attribute): " + str(r(total_blender)))
        

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
    print("\n--------------- AREA -----------------")
    get_area(mesh)
    print("-------------------------------------------------") 

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


if __name__ == "__main__":
   main()