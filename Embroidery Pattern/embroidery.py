# Embroidery Stitching Program by Nico Aldana & Silvester Nava c2023
import turtle

# Global variables
s = 10 # Scale factor mm to stitch coordinates, may not be necessary

# In millimeters (eventually replace with user input)
width = 1.0 # mm
dz = 0.2 # mm

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

def overstitch(w, dz, start_x, start_y, end_x, end_y):
    # Convert mm to stitches
    w = int(w*s) # Width of overstitch
    dz = int(dz*s) # "Tightness" of stitch

    stitch_output = [] # Starting stitch

    # Check if direction of stitch is horizontal or vertical
    dy = end_y - start_y
    dx = end_x - start_x
    
    if dx >= -1 and dx <= 1: # Vertical case
        print("dy: " + str(dy))
        n = abs(int(int(dy/dz)/2)) # Number of iterations to generate stitch coordinates
        if dy > 0: # Check direction of stitching
            for i in range(0, n):
                stitch_output += [w, dz,]
                stitch_output += [256 - w, dz,]
        else:
            for i in range(0, n):
                stitch_output += [w, 256 - dz,]
                stitch_output += [256 - w, 256 - dz,]
    elif dy >= -1 and dy <= 1: # Horizontal case
        print("dx: " + str(dx))
        n = abs(int(int(dx/dz)/2))
        if dx > 0:
            offset = abs(int(int(w/dz)/2))
            for i in range(0, n + offset):
                stitch_output += [dz, w,]
                stitch_output += [dz, 256 - w,]
        else:
            for i in range(0, n):
                stitch_output += [256 - dz, w,]
                stitch_output += [256 - dz, 256 - w,]
    else:
        print("Error: diagonal line?")
    return stitch_output

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Hilbert Curve")
t = turtle.Turtle()
t.speed(0)
# Draw the curve
t.penup()
t.goto(0, 0)
t.pendown()

points = []
hilbert_curve(t, order=5, size=30, direction=1, angle=90, points=points)
print(points)

# Keep the screen open
turtle.done()
# Generate file
stitches = [128, 2, 0, 0, 128, 128,] # Start at(0,0)

# Overstitch along the path
for i in range(0, len(points) - 1):
    stitches += overstitch(width, dz, points[i][0], points[i][1], points[i+1][0], points[i+1][1])
#stitches += overstitch(width, dz, 0, 0, 0, -100)

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
with open("test.jef", "wb") as f:
    f.write(jefBytes)


