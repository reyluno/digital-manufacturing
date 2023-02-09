import cairo as c
import math

# Hard code values for now

length, width, height = 1, 1, 1

thickness = 0.25 # Change according to acrylic thickness

# length = float(input("Enter a length of your desired box: "))
# # add code to validate data entry later
# width = float(input("Enter a width of your desired box: "))
# height = float(input("Enter a height for your desired box: "))

inc = length/5

WIDTH, HEIGHT = 1000, 1000

start_x, start_y = 0.1, 0.1

surface = c.SVGSurface("example.svg", WIDTH, HEIGHT)
ctx = c.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

# ctx.rectangle(0, 0, 1,              1)  # Rectangle(x0, y0, x1, y1)

# ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(0.0, 0.0)
ctx.move_to(start_x, start_y)

ctx.line_to(start_x + inc, start_y)
ctx.line_to(start_x + inc, start_y + thickness)
ctx.line_to(start_x + 2*inc, start_y + thickness)
ctx.line_to(start_x + 2*inc, start_y)
# Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
#ctx.close_path()

ctx.set_source_rgb(0.0, 0.0, 0.0)  # Solid color
ctx.set_line_width(0.01)
ctx.stroke()



