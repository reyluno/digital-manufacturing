import math

# User-inputted parameters
L = float(input("Enter the length of the triangles (L): "))
theta = float(input("Enter the rotation angle of the triangles (theta in degrees): "))
Z = float(input("Enter the height between layers (Z): "))

# Convert theta from degrees to radians
theta = math.radians(theta)
n = 10 # Number of triangles
EXTRUSION = 0.8
FEEDRATE = 200

# Open a Gcode file for writing
with open("pyramid.gcode", "w") as f:
    # Write initial Gcode commands for setting up the CNC machine
    f.write("G90 ; Set to absolute positioning mode\n")
    f.write("G21 ; Set to millimeter units\n")
    f.write("G28 ; Home all axes\n")
    f.write("G1 X100 Y50 Z3.5 F500 ; Move to the starting point (X=0, Y=0, Z=0) at a feedrate of 1000mm/min\n")
    f.write("G92 X0 Y0 Z0 E0\n")
    #f.write("G91\n")


    # Loop through each layer of triangles
    z = 0
    alpha = 0

    for i in range(0, n):
        # Loop through each triangle in the layer
        for i in range(1):
            # Calculate the vertices of the triangle in the current layer
            x1 = L * math.cos(i * 2 * math.pi / 3)
            y1 = L * math.sin(i * 2 * math.pi / 3)
            x2 = L * math.cos((i + 1) * 2 * math.pi / 3)
            y2 = L * math.sin((i + 1) * 2 * math.pi / 3)
            x3 = L * math.cos((i + 2) * 2 * math.pi / 3)
            y3 = L * math.sin((i + 2) * 2 * math.pi / 3)

            # Rotate the vertices of the triangle by theta
            x1_rot = x1 * math.cos(alpha) - y1 * math.sin(alpha)
            y1_rot = x1 * math.sin(alpha) + y1 * math.cos(alpha)
            x2_rot = x2 * math.cos(alpha) - y2 * math.sin(alpha)
            y2_rot = x2 * math.sin(alpha) + y2 * math.cos(alpha)
            x3_rot = x3 * math.cos(alpha) - y3 * math.sin(alpha)
            y3_rot = x3 * math.sin(alpha) + y3 * math.cos(alpha)

            # Write Gcode commands for moving to the vertices of the triangle
            f.write("G1 X{} Y{} Z{} E{}; Move to vertex 1 of the triangle\n".format(x1_rot, y1_rot, z, EXTRUSION))
            f.write("G1 X{} Y{} Z{} E{} ; Move to vertex 2 of the triangle\n".format(x2_rot, y2_rot, z, EXTRUSION))
            f.write("G1 X{} Y{} Z{} E{} ; Move to vertex 3 of the triangle\n".format(x3_rot, y3_rot, z, EXTRUSION))
            f.write("G1 X{} Y{} Z{} E{} ; Move back to vertex 1 of the triangle\n".format(x1_rot, y1_rot, z, EXTRUSION))

        # Move up to the next layer
        z += Z
        alpha += theta
        f.write("G1 Z{} ; Move up to the next layer\n".format(z))

    # Write Gcode commands for returning to the home position and ending the program
    f.write("G1 Z15\n")
    #f.write("G1 X0 Y0 Z0 ; Move back to the home position\n")
    #f.write("G28 ; Home all axes\n")
    f.write("M2 ; End of program\n")
