import bpy 
from time import time
import mathutils
import sys, os
sys.path.append(os.getcwd())
print(os.getcwd())
from utils import r

def get_valences(me):

    valence_max = 0
    valence_min = float('Inf')

    valences = [0 for i in range(len(me.vertices))]
    for edge in me.edges:
        valences[edge.vertices[0]] += 1
        valences[edge.vertices[1]] += 1
    
    valences_sum = 0    
    for valence in valences:
        if (valence > valence_max):
          valence_max = valence
        if (valence < valence_min):
          valence_min = valence
          
        valences_sum += valence
          
    valence_avg = valences_sum / len(valences)
    
    return [valence_avg, valence_max, valence_min]


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
    valence_avg, valence_max, valence_min = [r(get_valences(mesh)[i]) for i in range(3)]
    print("\n--------------- VALENCES ---------------")
    print("Average Valence: " + str(valence_avg))
    print("Max Valence: " + str(valence_max))
    print("Min Valence: " + str(valence_min))
    print("----------------------------------------------")

    # Report performance...
    print("Script took %6.3f secs.\n\n"%(time()-t))


# main()