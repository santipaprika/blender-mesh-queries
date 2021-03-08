import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
from utils import r
from manifolds import get_manifolds
from numpy import cross

def get_convexity(me):

    manifold_edges = get_manifolds(me)
              
    convex_edges = []
    concave_edges = []

    # print(' -> '.join(str(me.loops[me.polygons[manifold_edges.values()[0][0]].loop_indices[i]].vertex_index) for i in range(4)))
    # print(' -> '.join(str(me.loops[me.polygons[manifold_edges.values()[0][1]].loop_indices[i]].vertex_index) for i in range(4)))

    # print(me.polygons[manifold_edges[0][0]].edge_keys)
    # print(me.polygons[manifold_edges[0][1]].edge_keys)

    for key, value in manifold_edges.items():
        num_face_loops = me.polygons[value[0]].loop_total
        print("Edge " + str(key))
        print(' -> '.join(str(me.loops[me.polygons[value[0]].loop_indices[i]].vertex_index) for i in range(num_face_loops)))
        #print(' -> '.join(str(me.loops[me.polygons[value[1]].loop_indices[i]].vertex_index) for i in range(num_face_loops)))

        # O(num_face_loops): average case, num_face_loops << total number of vertices, which approximates to O(1)
        # e.g. regular quad mesh will be O(4). 
        # Worst case where mesh has a polygon with a lot of vertices while other polygons do not, then it is closer to O(n),
        # but only for this specific polygon

        for loop_idx in range(num_face_loops):
            vertex_idx = me.loops[me.polygons[value[0]].loop_indices[loop_idx]].vertex_index
            if vertex_idx == key[0]:
                vertex_p_idx = me.loops[me.polygons[value[0]].loop_indices[(loop_idx+1)%num_face_loops]].vertex_index
                if vertex_p_idx == key[1]:
                    # current face is left-hand's one
                    print("First is LEFT")
                    print("LEFT NORMAL: " + str(me.polygons[value[0]].normal) + " || RIGHT NORMAL " + str(me.polygons[value[1]].normal))
                    print("Edge Vector: " + str(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co))
                    print("Vertex " + str(vertex_idx) + " (origin): " + str(me.vertices[vertex_idx].co))
                    print("Vertex " + str(vertex_p_idx) + " (dest): " + str(me.vertices[vertex_p_idx].co))
                    print(" ")

                    normals_cp = cross(me.polygons[value[0]].normal, me.polygons[value[1]].normal)
                    print("CROSS NORMAL: " + str(normals_cp))
                    convex_edges.append(key) if normals_cp.dot(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co) >= 0 else concave_edges.append(key)
                    print(normals_cp.dot(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co))

                else:
                    vertex_p_idx = me.loops[me.polygons[value[0]].loop_indices[(loop_idx-1)%num_face_loops]].vertex_index
                    # current face is right-hand's one
                    print("First is RIGHT")
                    print("LEFT NORMAL: " + str(me.polygons[value[1]].normal) + " || RIGHT NORMAL " + str(me.polygons[value[0]].normal))
                    print("Edge Vector: " + str(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co))
                    print("Vertex " + str(vertex_idx) + " (origin): " + str(me.vertices[vertex_idx].co))
                    print("Vertex " + str(vertex_p_idx) + " (dest): " + str(me.vertices[vertex_p_idx].co))
                    print(" ")


                    normals_cp = cross(me.polygons[value[1]].normal, me.polygons[value[0]].normal)
                    print("CROSS NORMAL: " + str(normals_cp))

                    convex_edges.append(key) if normals_cp.dot(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co) >= 0 else concave_edges.append(key)
                    print(normals_cp.dot(me.vertices[vertex_p_idx].co - me.vertices[vertex_idx].co))
                
                
                break
            



    print("\n--------------- Ex 5. CONVEXITY -----------------")
    print("Convex edges: " + str(len(convex_edges)))
    print("Concave edges: " + str(len(concave_edges)))
    #print("Non Manifold edges: " + str(non_manifolds))
    print("-------------------------------------------------")

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
    get_convexity(mesh)

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


main()