# Lampshade Lattice Generator by Nico Aldana and Silvester Nava c2023
# For use in Blender ONLY

import bpy, bmesh
import math, mathutils, random

# Define initial parameters
rp = 3.5 # Bottom radius so that we can fit the tea light
R = math.sqrt((9/5)*rp**2) # Radius of bounding sphere
H = (5/3)*R # Height of lampshade

n = 5 # Number of "levels" of the sphere
h = H/n # Layer height

# Torus specifications
torus_radius = 1.0
torus_thickness = 0.2

def generate_lampshade():
    nodes = []
    phi = [45] # Angle of base layer
    quantities = []
    for i in range(0,n): # Calculate RP and z for each level of the sphere
        nodes.append([curve(i*h),i*h]) # (RP, z)
    print(nodes)
    for i in range(0,n-1): # Calculate angles to tilt each level of the sphere
        phi.append(math.degrees(math.atan((nodes[i+1][1] - nodes[i][1]) / (nodes[i+1][0] - nodes[i][0]))))
    for i in range(0,n): # Calculate how many tori per level
        if(i == 0): # Have the base layer be slightly denser
            quantities.append(int((3/2)*math.pi*(nodes[i][0])/(torus_radius/3)))
        else:
            quantities.append(int((3/2)*math.pi*(nodes[i][0])/torus_radius))
    for i in range(0,n):
        if(i == 0): # Make sure the base layer tori are smaller and thicker for good ground support
            create_tori(quantities[i], nodes[i][0], torus_radius/3, phi[i], nodes[i][1],torus_thickness*2,phi[i])
        else:
            create_tori(quantities[i], nodes[i][0], torus_radius, phi[i], nodes[i][1],torus_thickness,phi[i])
    # Generate lampshade ceiling (optional)    
    create_tori(8, rp/2, torus_radius, 45, H, torus_thickness, -30) 
            
def print(data): # This is just so that we can print to the Blender console LOL
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT") 

def curve(z): # Define the equation following the curve of the spherical lampshade
    return math.sqrt(R**2 - (z - (2/3)*R)**2)

def create_tori(n, RP, r, theta, z, t, phi): # Function that creates the ring of tori for each layer
    # Set the origin of the scene to (0, 0, z)
    bpy.context.scene.cursor.location = (0, 0, z)
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
    
    # Determine subdivision count to smooth the model (Recommended: 2-3)
    subdivisions = 3

    for i in range(n):
        # Calculate the angle for the current torus
        angle = 2 * math.pi * i / n
        
        # Calculate the x and y coordinates for the current torus along a circle of radius RP
        x = RP * math.cos(angle + math.pi/2)
        y = RP * math.sin(angle + math.pi/2)
        
        # Calculate the normal vector to the tangent plane for the current torus
        normal = mathutils.Vector((x, y, z)).normalized()
        
        # Scale the major and minor radii of the torus to create an oblong shape
        s = 1.3 # Recommended: 0.8 - 1.3
        major_radius = r * s
        minor_radius = t / s

        # Create the torus object relative to the origin
        bpy.ops.mesh.primitive_torus_add(location=(x, y, 0), rotation=(0, 0, angle + math.pi/2), major_radius=major_radius, minor_radius=minor_radius)
        torus = bpy.context.object
        
        # Move the torus to the correct z position
        torus.location.z = z

        # Parent the torus to the empty object at the origin
        torus.parent = bpy.context.scene.objects["Empty"]
        
        # Rotate the torus outward along the z-axis
        torus.rotation_euler[2] = theta
        
        # Calculate the rotation axis for the tilt of the torus
        axis = mathutils.Vector((x, y, z)).normalized().cross(mathutils.Vector((0, 0, 1)))
        
        # If the axis vector is close to zero, set it to a default direction
        if axis.length < 1e-5:
            axis = mathutils.Vector((1, 0, 0))
        
        # Calculate the angle for the tilt of the torus
        angle = math.radians(phi)
        
        # Create the rotation quaternion for the tilt of the torus
        rot_quat = mathutils.Quaternion(axis, angle)
        
        # Rotate the torus to perform the tilt
        torus.rotation_mode = 'QUATERNION'
        torus.rotation_quaternion = rot_quat
        
        # Add a subdivision surface modifier to the torus
        mod = torus.modifiers.new("Subdivision", 'SUBSURF')
        mod.levels = subdivisions

generate_lampshade() # Run the program
