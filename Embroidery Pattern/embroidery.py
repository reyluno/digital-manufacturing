# Embroidery Stitching Program by Nico Aldana & Silvester Nava c2023
import turtle, math
from PIL import Image
import numpy as np

# Some quick notes about generating files:

##################
## JUMP COMMAND ## --> # stitches += [128, 2, dx, dy,]
##################

##################
## TRIM COMMAND ## --> stitches += [128, 128, dx, dy,]
##################

# Global variables
points = [] # List that tracks all the turning points of the Hilbert Curve
interpolated_path = [] # List that plots the Hilbert Curve as a continuous path

# In 0.1 millimeters
w = int(input("Enter a width for each stitch, in 0.1 mm (Recommended: 10): "))
dz = int(input("Enter a tightness for each stitch (Recommended: 2): "))

userOrder = int(input("Enter an order size for the pattern (Recommended: 6): "))
userSize = int(input("Enter a step size for the pattern (Recommended: 30): "))

# w = 10 # Width of overstitch (10)
# dz = 2 # Tightness of stitch (2)

# Generate Hilbert Curve
def hilbert_curve(t, order, size, direction, angle, points):
    if order == 0:
        return
    # Recursively draw the curve
    t.right(direction * angle)
    hilbert_curve(t, order - 1, size, -direction, angle, points)
    t.forward(size)
    x, y = map(int, t.position())
    points.append((x, y))
    t.left(direction * angle)
    hilbert_curve(t, order - 1, size, direction, angle, points)
    t.forward(size)
    x, y = map(int, t.position())
    points.append((x, y))
    hilbert_curve(t, order - 1, size, direction, angle, points)
    t.left(direction * angle)
    t.forward(size)
    x, y = map(int, t.position())
    points.append((x, y))
    hilbert_curve(t, order - 1, size, -direction, angle, points)
    t.right(direction * angle)

# Function to handle vertical and horizontal overstitching
def overstitch(start, end):
    stitch_output = [] # Starting stitch
    # Check if direction of stitch is horizontal or vertical
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    if dx >= -1 and dx <= 1: # Vertical case
        n = abs(int(int(dy/dz)/2)) # Number of iterations to generate stitch coordinates
        # Check direction of stitching
        if dy > 0: # 8 ^
            stitch_output += [256 - int(w/2), 0]
            for i in range(0, n):
                stitch_output += [w, dz,]
                stitch_output += [256 - w, dz,]
            stitch_output += [int(w/2), 0]
        else: # 2 v
            stitch_output += [256 - int(w/2), 0]
            for i in range(0, n):
                stitch_output += [w, 256 - dz,]
                stitch_output += [256 - w, 256 - dz,]
            stitch_output += [int(w/2), 0]
    elif dy >= -1 and dy <= 1: # Horizontal case
        n = abs(int(int(dx/dz)/2))
        if dx > 0: # -> 6
            stitch_output += [0, 256 - int(w/2)]
            for i in range(0, n):
                stitch_output += [dz, w,]
                stitch_output += [dz, 256 - w,]
            stitch_output += [0, int(w/2)]
        else: # 4 <-
            stitch_output += [0, 256 - int(w/2)]
            for i in range(0, n):
                stitch_output += [256 - dz, w,]
                stitch_output += [256 - dz, 256 - w,]
            stitch_output += [0, int(w/2)]
    else: # Jump case
        if abs(dx) > 127:
            #print("Incoming jump in X")
            n1 = abs(int(dx/127)) # number of times to jump
        else: n1 = 1
        if abs(dy) > 127:
            #print("Incoming jump in Y")
            n2 = abs(int(dy/127))
        else: n2 = 1

        if n1 == 1 and n2 == 1: # If small jump:
            if dx < 0 and dy > 0: # Jumping NW
                stitch_output += [128, 2, 256 + dx, dy,]
            if dx > 0 and dy < 0: # Jumping SE
                stitch_output += [128, 2, dx, 256 + dy,]
            if dx < 0 and dy < 0: # Jumping SW
                stitch_output += [128, 2, 256 + dx, 256 + dy,]
            if dx > 0 and dy > 0: # Jumping NE
                stitch_output += [128, 2, dx, dy,]
        else:  
            print("Big jump...")
            if dx < 0 and dy > 0: # Jumping NW
                print("Jumping northwest.")
                for i in range(n1):
                    stitch_output += [128, 2, 256 + int(dx/n1), 128,]
                for i in range(n2):
                    stitch_output += [128, 2, 128, int(dy/n2),]
            elif dx > 0 and dy < 0: # Jumping SE
                print("Jumping southeast.")
                for i in range(n1):
                    stitch_output += [128, 2, int(dx/n1), 128,]
                for i in range(n2):
                    stitch_output += [128, 2, 128, 256 + int(dy/n2),]
            elif dx < 0 and dy < 0: # Jumping SW
                print("Jumping southwest.")
                for i in range(n1):
                    stitch_output += [128, 2, 256 + int(dx/n1), 128,]
                for i in range(n2):
                    stitch_output += [128, 2, 128, 256 + int(dy/n2),]
            elif dx > 0 and dy > 0: # Jumping NE
                print("Jumping northeast.")
                for i in range(n1):
                    stitch_output += [128, 2, int(dx/n1), 128,]
                for i in range(n2):
                    stitch_output += [128, 2, 128, int(dy/n2),]
            else:
                print("error?")
    return stitch_output

# Function to interpolate coordinates
def interpolate(coords, n):
    interpolated_coords = []
    for i in range(len(coords) - 1):
        x0, y0 = coords[i]
        x1, y1 = coords[i+1]
        dx = (x1 - x0) / (n+1)
        dy = (y1 - y0) / (n+1)
        for j in range(n):
            x = int(x0 + dx * (j+1))
            y = int(y0 + dy * (j+1))
            interpolated_coords.append((x, y))
    return interpolated_coords



# Draw the Hilbert Curve in turtle
def draw():
    screen = turtle.Screen()
    screen.setup(width=2000, height=2000)
    screen.title("Hilbert Curve")
    t = turtle.Turtle()
    t.speed(0)
    # Draw the curve
    t.penup()
    t.goto(0, 0)
    t.pendown()
    hilbert_curve(t, order=userOrder, size=userSize, direction=1, angle=90, points=points) # Generate points
    turtle.bye()
    
draw()

# Save the list of points as a csv for debugging
np.savetxt("points.csv", points, delimiter =", ", fmt ='% s')

# Get the interpolated path
interpolated_path = interpolate(points, 5)

# Find bounding box of the pattern
def find_max_coordinates(coords):
    max_x = max(coords, key=lambda item: item[0])[0]
    min_y = min(coords, key=lambda item: item[1])[1]
    return max_x, min_y

max_x, min_y = find_max_coordinates(points)

# Function for filtering out coordinates outside of circle
def filter_coordinates(coords, R, h, k):
    filtered_coords = []
    for x, y in coords:
        distance = math.sqrt((x-h)**2 + (y-k)**2)
        if distance <= R:
            filtered_coords.append((x, y))
    return filtered_coords

# Filter out coordinates
new_list = filter_coordinates(interpolated_path, 300, max_x * 0.5, min_y *  0.5)

# Save csv for debugging
np.savetxt("newlist.csv", new_list, delimiter =", ", fmt ='% s')
# Generate file
stitches = [128, 2, 0, 0, 128, 128,]

# Generate stitches
for i in range(0, len(points) - 1):
    stitches += overstitch(points[i], points[i+1])

# Experimental ...
# for i in range(0, len(new_list) - 1):
#     stitches += overstitch(new_list[i], new_list[i+1])

stitches += [128, 16] # Last stitch command

jefBytes = [124, 0, 0, 0, # Byte offset of the first stitch
            10, 0, 0, 0, # Unknown number
            ord("2"), ord("0"), ord("2"), ord("3"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("2"), # MMDD
            ord("1"), ord("6"), ord("2"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0, # SS00
            1, 0, 0, 0, # Number of physical threads (1)
            (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0, # Number of stitches
            3, 0, 0, 0, # Sewing machine hoop
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            32, 0, 0, 0, # Thread color (2 = White)
            13, 0, 0, 0, # Unknown number
            ] + stitches

jefBytes = bytes(jefBytes)
with open("pattern.jef", "wb") as f:
    f.write(jefBytes)


