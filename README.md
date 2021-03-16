# Blender Mesh Queries
Lab projects for the advanced 3D modeling course in MIRI, at UPC.
A collection of mesh queries are implemented as different modules (which may depend on each other).

## How to run
To execute a python module *my_module.py* with a given blender project *my_project.blend* as context,
use the following command directly in terminal (tested on Windows 10):
```
blender path/to/my_project.blend --background --python path/to/my_module.py
```
Where the paths are relative to the current folder where the command is being executed.

e.g. if we want to run the *genus.py* module on the *torus.blend* model (running the command from the root repository folder):
```
blender models/torus.blend --background --python modules/genus.py
```
## Modules
### centroid.py
Computes the centroid of the selected mesh.

### valences.py
Computes and prints out the minimum, maximum and average valence of all vertices in the selected mesh.

### manifold.py
Computes and prints the number of boundary, manifold and non-manifold edges in the selected model.

### shells.py
Computes and prints the number of shells of the selected object.

### genus.py
Computes and prints the number of genus of the selected object.

### area.py
Compute the surface area the selected object (and each of its faces).

### volume_eberly.py
Compute (and to print) the total volume of the selected object using [Eberly's approach](https://www.cs.upc.edu/~virtual/SGI/docs/3.%20Further%20Reading/Polyhedral%20Mass%20Properties%20Revisited.pdf). Different connected components are added, but shells that do not form a 2-manifold without boundary are ignored. 

### Volume_zhang.py
Compute (and to print) the total volume of the selected object using [Zhang's approach](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.20.9775&rep=rep1&type=pdf). Different connected components are added, but shells that do not form a 2-manifold without boundary are ignored. 
