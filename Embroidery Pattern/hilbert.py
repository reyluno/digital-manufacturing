import turtle
import math

def hilbert_curve(n, angle=90, d=20, start_x=0, start_y=0, max_radius=None):
    if max_radius is not None:
        distance = math.sqrt((turtle.xcor() - start_x) ** 2 + (turtle.ycor() - start_y) ** 2)
        if distance > max_radius:
            return []
    if n <= 0:
        return [(turtle.xcor(), turtle.ycor())]
    turtle.right(angle)
    coords = hilbert_curve(n-1, -angle, d, start_x, start_y, max_radius)
    turtle.forward(d)
    coords += hilbert_curve(n-1, angle, d, start_x, start_y, max_radius)
    turtle.left(angle)
    turtle.forward(d)
    coords += hilbert_curve(n-1, angle, d, start_x, start_y, max_radius)
    turtle.left(-angle)
    turtle.forward(d)
    coords += hilbert_curve(n-1, -angle, d, start_x, start_y, max_radius)
    turtle.right(-angle)
    return coords

# Set up the turtle and canvas
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

# User input for the center and radius of the circle
center_x = float(input("Enter x-coordinate of center: "))
center_y = float(input("Enter y-coordinate of center: "))
R = float(input("Enter radius of circle: "))

d = 20
# Generate the Hilbert Curve coordinates within the circle
curve_coords = []
for x in range(int(center_x - R), int(center_x + R) + 1, d):
    for y in range(int(center_y - R), int(center_y + R) + 1, d):
        if math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= R:
            turtle.goto(x, y)
            curve_coords += hilbert_curve(4, d=10, start_x=x, start_y=y, max_radius=R)

# Draw the Hilbert Curve
turtle.penup()
turtle.goto(curve_coords[0])
turtle.pendown()
for coord in curve_coords:
    turtle.goto(coord)

# Save the Hilbert Curve coordinates to a file
with open("hilbert_curve.txt", "w") as f:
    for coord in curve_coords:
        f.write(f"{coord[0]}, {coord[1]}\n")

# Keep the turtle window open until it is manually closed
turtle.mainloop()
