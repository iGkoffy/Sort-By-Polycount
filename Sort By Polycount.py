import bpy

# Function to get the polycount of a mesh object
def get_polycount(obj)
    if obj.type == 'MESH'
        return len(obj.data.polygons)
    return 0

# Add polycount at the beginning of the object names in the Outliner
def add_polycount_to_names()
    for obj in bpy.context.scene.objects
        if obj.type == 'MESH'
            polycount = get_polycount(obj)
            # Update object name with the polycount at the beginning (e.g., [456 polys] Cube)
            obj.name = f[{polycount} polys] {obj.name.split(']')[-1].strip()}

# Run the function
add_polycount_to_names()
