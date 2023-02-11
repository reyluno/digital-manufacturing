# Master Desk Organizer Code by Nico Aldana and Silvester Nava
import math

# Validates data input
def check_input(lower, upper, prompt):
    while True:
        try:
            user_input = int(input(f"{prompt}"))
            if lower <= user_input <= upper:
                return user_input
            else:
                print("The number is not within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

print("Welcome to Nico & Silvester's Desk Organizer Generator! Please enter parameters. All measurements are in millimeters.")
# User inputted variables
d = check_input(90, 110, "Please input an overall depth for the container (Recommended: 90-110 mm): ")
L = check_input(125, 150, "Please input an overall length for the container (Recommended: 125-150 mm): ")
hp = check_input(120, 150, "Please input a height for the pencil holder (Recommended: 120-150 mm): ")

baseText = input("Please enter text you'd like engraved on the base of the organizer: ") # Determine char max
fontSize = 10
if(len(baseText) > 5):
    fontSize = 8
frontText = input("Please enter text you'd like engraved on the front of the container: ") # Determine char max

# Global variables
H = 300 # Overall height
t = 3.175 # Acrylic thickness

# Derived variables
r = d/2 # Half overall width
l = L - r # Length of pencil-holder segment
h = H - r # Vertical height of spine
dp = d-2*t # Adjusted piece width

# Header for svg document
starter = "<!-- Desk Organizer SVG by Nico Aldana and Silvester Nava c2023 -->\n<!-- Scale: 1:1 pixels to mm -->\n"
starter += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="305" height="457">\n'
output = starter

# Create base piece svg
def Base(): 
    baseOutput = output # Instantiate svg with the same basic starter
    baseOutput += f'<path d="M5 5 l{dp} 0 l0 {l} l{t} 0 a{r} {r} 0 0 1 {-2*r} 0 l{t} 0 l{0} {-l}" stroke="black" stroke-width="1" fill="none"/>'
    baseOutput += f'<rect x="{5+dp/3}" y="{5+l}" width="{dp/3}" height="{t}" stroke="black" stroke-width="1" fill="none"/>'

    # User-specified text
    baseOutput += '<style type="text/css">.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}.st1{font-family:\'LEMONMILK-Bold\';}.st2{font-size:'
    baseOutput += f'{fontSize}px;'
    baseOutput += '}</style>'
    baseOutput += f'<text x="{r}" y="{l+r/2}" dominant-baseline="middle" text-anchor="middle" class="st1 st2">{baseText}</text>'
    # End svg
    baseOutput += '\n</svg>'
    f = open('base.svg', 'w')
    f.write(baseOutput)

# Create spine piece svg
def Spine():
    # Derived measurements:
    rectX = 5 + (d-20)/2
    rectY = 5 + r/3
    tabX = 5 + (d-30)/2
    tabY = 5 + h + r/3

    spineOutput = output
    spineOutput += f'<path d="M5 {5+r} a{r} {r} 0 0 1 {2*r} 0 l0 {h} l{-(d-dp/3)/2} 0 l0 {t} l{-dp/3} 0 l0 {-t} l{-(d-dp/3)/2} 0 l0 {-h}" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<rect x="{rectX}" y="{rectY}" width="20" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
    # ADD CIRCLES FOR SCREW HOLES HERE

    # Generate tab cutout
    spineOutput += f'<path d="M{tabX} {tabY} l30 0 l0 -5 l-5 0 l0 -40 l-20 0 l0 40 l-5 0 l0 5" stroke="black" stroke-width="1" fill="none"/>'

    # Generate fractal pattern
    spineOutput += Fractal()
    spineOutput += '\n</svg>'
    f = open('spine.svg', 'w')
    f.write(spineOutput)

def Sides():
    sideOutput = output
    sideOutput += f'<rect x="5" y="5" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + l}" y="5" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'

    sideOutput += f'<rect x="{5 + 2*l}" y="5" width="{d}" height="{hp}" stroke="black" stroke-width="1" fill="none" />' # Front panel
    sideOutput += '<style type="text/css">.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}.st1{font-family:\'LEMONMILK-Bold\';}.st2{font-size:10px;}.st3{font-size:7px;}</style>'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/4}" dominant-baseline="middle" text-anchor="middle" class="st1 st2">{frontText}</text>'

    # Add SEAS logo + Digital Manufacturing
    sideOutput += f'<image x="{5 + 2*l + d/2 - 10}" y="{hp/3 + 10}" width="20" height="22.3" xlink:href="seas.svg" />'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/3 + 45}" dominant-baseline="middle" text-anchor="middle" class="st1 st3">Digital</text>'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/3 + 55}" dominant-baseline="middle" text-anchor="middle" class="st1 st3">Manufacturing</text>'

    # ADD CIRCLES AND SCREW CONTOURS

    sideOutput += '\n</svg>'
    f = open('sides.svg', 'w')
    f.write(sideOutput)

# Generates fractal pattern
def fractal_koch(x1, y1, x2, y2, depth):
    if depth == 0:
        return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='black' stroke-width='1' />"
    angle = math.radians(60)
    x3 = x1 + (x2 - x1) / 3
    y3 = y1 + (y2 - y1) / 3
    x4 = x1 + (x2 - x1) * 2 / 3
    y4 = y1 + (y2 - y1) * 2 / 3
    x5 = x3 + (x4 - x3) * math.cos(angle) + (y4 - y3) * math.sin(angle)
    y5 = y3 - (x4 - x3) * math.sin(angle) + (y4 - y3) * math.cos(angle)
    result = fractal_koch(x1, y1, x3, y3, depth - 1)
    result += fractal_koch(x3, y3, x5, y5, depth - 1)
    result += fractal_koch(x5, y5, x4, y4, depth - 1)
    result += fractal_koch(x4, y4, x2, y2, depth - 1)
    return result

# Generates fractal as svg
def Fractal():
    center_x = r
    center_y = 3*r/2
    radius = r/2
    pattern = ""
    for i in range(6):
        angle1 = math.radians(60 * i)
        angle2 = math.radians(60 * (i + 1))
        x1 = center_x + radius * math.cos(angle1)
        y1 = center_y + radius * math.sin(angle1)
        x2 = center_x + radius * math.cos(angle2)
        y2 = center_y + radius * math.sin(angle2)
        pattern += fractal_koch(x1, y1, x2, y2, 5)
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' width='{d}' height='{h+r}'>{pattern}</svg>"
    f = open('snowflake.svg','w')
    f.write(svg)
    fractal = f'<image x="5" y="0" xlink:href="snowflake.svg" />'
    return fractal


# Create 
Base()
Spine()
Sides()