import turtle

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

def main():
    # Set up the turtle screen and object
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
    hilbert_curve(t, order=4, size=15, direction=1, angle=90, points=points)
    print(points)

    # Keep the screen open
    turtle.done()

if __name__ == "__main__":
    main()
