import turtle

def hilbert_curve(n, angle=90, d=10, start_x=0, start_y=0):
    if n <= 0:
        return [(start_x, start_y)]
    coords = []
    turtle.goto(start_x, start_y)
    turtle.right(angle)
    coords += hilbert_curve(n-1, -angle, d, turtle.xcor(), turtle.ycor())
    turtle.forward(d)
    coords += [(turtle.xcor(), turtle.ycor())]
    turtle.left(angle)
    coords += hilbert_curve(n-1, angle, d, turtle.xcor(), turtle.ycor())
    turtle.forward(d)
    coords += [(turtle.xcor(), turtle.ycor())]
    coords += hilbert_curve(n-1, angle, d, turtle.xcor(), turtle.ycor())
    turtle.left(angle)
    coords += [(turtle.xcor(), turtle.ycor())]
    turtle.forward(d)
    coords += hilbert_curve(n-1, -angle, d, turtle.xcor(), turtle.ycor())
    turtle.right(angle)
    return coords

# Set up the turtle and canvas
turtle.screensize(canvwidth=100, canvheight=100, bg=None)
turtle.speed(0)
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()
turtle.hideturtle()
turtle.tracer(0)

# Generate the Hilbert Curve coordinates
curve_coords = hilbert_curve(5, d=5, start_x=0, start_y=0)

# Draw the Hilbert Curve
for coord in curve_coords:
    turtle.goto(coord)

# Update the canvas
turtle.update()

# Save the Hilbert Curve coordinates to a file
with open("hilbert_curve.txt", "w") as f:
    for coord in curve_coords:
        f.write(f"{coord[0]}, {coord[1]}\n")

# Keep the turtle window open until it is manually closed
turtle.mainloop()
