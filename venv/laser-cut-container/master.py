# Master Desk Organizer Code by Nico Aldana and Silvester Nava c2023
import math, random

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
d = check_input(80, 105, "Please input an overall depth for the container (Recommended: 80-105 mm): ")
L = check_input(120, 150, "Please input an overall length for the container (Recommended: 120-150 mm): ")
hp = check_input(100, 140, "Please input a height for the pencil holder (Recommended: 100-140 mm): ")
baseText = input("Please enter text you'd like engraved on the base of the organizer: ") 
frontText = input("Please enter text you'd like engraved on the front of the container: ")

# Determine appropriate font size for text length
baseFontSize = 10
frontFontSize = 10
if(len(baseText) > 6):
    baseFontSize = 7
if(len(frontText) > 6):
    frontFontSize = 7

# Global variables
H = 300 # Overall height
t = 3.175 # Acrylic thickness
margin = 2 # Margin between pieces

# Derived variables
r = d/2 # Half overall width
l = L - r # Length of pencil-holder segment
h = H - r # Vertical height of spine
dp = d-2 * t # Adjusted piece width
w = d - 2*t # Adjusted lid width

# Header for svg document
starter = "<!-- Desk Organizer SVG by Nico Aldana and Silvester Nava c2023 -->\n<!-- Scale: 1:1 pts to mm -->\n"
starter += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="305" height="457">\n'

# Create base piece paths
def Base():
    xOffset = 5 + d + t + margin
    baseOutput = f'<path d="M{xOffset} 5 l{dp} 0 l0 {l} l{t} 0 a{r} {r} 0 0 1 {-2*r} 0 l{t} 0 l{0} {-l}" stroke="black" stroke-width="1" fill="none"/>'
    baseOutput += f'<rect x="{xOffset+dp/3}" y="{5+l}" width="{dp/3}" height="{t}" stroke="black" stroke-width="1" fill="none"/>'

    # User-specified text
    baseOutput += '<style type="text/css">.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}.st1{font-family:\'LEMONMILK-Bold\';}.st2{font-size:'
    baseOutput += f'{baseFontSize}px;'
    baseOutput += '}</style>'
    baseOutput += f'<text x="{xOffset - t + r}" y="{l+r/2}" dominant-baseline="middle" text-anchor="middle" class="st2">{baseText}</text>'

    #Top Screwhole
    baseOutput += f'<path d="M{xOffset + dp/2} 5 h -1.1 v 3 h -1.3 v 1.6 h 1.3 v 1.8 h 2.2 v -1.8 h 1.5 v -1.6 h -1.5 v -3 h -1.1" stroke="black" stroke-width="1" fill="none"/>'
    #Left Screwholes
    baseOutput += f'<path d="M{xOffset} {5 + l/4} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    baseOutput += f'<path d="M{xOffset} {5 + 3*l/4} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    #Right Screwholes
    baseOutput += f'<path d="M{xOffset + dp} {5 + l/4} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    baseOutput += f'<path d="M{xOffset + dp} {5 + 3*l/4} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'

    return baseOutput

# Create spine piece paths
def Spine():
    # Derived measurements:
    rectX = 5 + (d-20)/2
    rectY = 5 + r/3
    tabX = 5 + (d-30)/2
    tabY = 5 + h + r/3

    spineOutput = f'<path d="M5 {5+r} a{r} {r} 0 0 1 {2*r} 0 l0 {h} l{-(d-dp/3)/2} 0 l0 {t} l{-dp/3} 0 l0 {-t} l{-(d-dp/3)/2} 0 l0 {-h}" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<rect x="{rectX}" y="{rectY}" width="20" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
    
    # Circle Screwholes
    spineOutput += f'<circle cx="{5+2.4}" cy="{5 + H + t - hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{5+2.4}" cy="{5 + H + t - hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{5 + H + t - 4*hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{5 + H + t - 4*hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'

    # Circle Screwholes adjusted
    spineOutput += f'<circle cx="{5+2.4}" cy="{H-0.8*hp+3.2+5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{5+2.4}" cy="{H-0.2*hp+3.2+5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{H-0.8*hp+3.2+5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{H-0.2*hp+3.2+5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'

    # Generate tab cutout
    spineOutput += f'<path d="M{tabX} {tabY} l30 0 l0 -5 l-5 0 l0 -40 l-20 0 l0 40 l-5 0 l0 5" stroke="black" stroke-width="1" fill="none"/>'

    # Generate fractal pattern
    spineOutput += generate_fractal()
    return spineOutput

# Generate side piece paths
def Sides():
    yOffset = 5 + H + t + margin

    # Rectangles
    sideOutput = f'<rect x="5" y="{5 + yOffset}" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + l}" y="{5 + yOffset}" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + 2*l}" y="{5 + yOffset}" width="{d}" height="{hp}" stroke="black" stroke-width="1" fill="none" />' # Front panel

    # Tab cutouts
    sideOutput += f'<path d="M{5 + l/3} {5 + yOffset} l0 {t} l{l/3} 0 l0 {-t}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<path d="M{5 + 4*l/3} {5 + yOffset} l0 {t} l{l/3} 0 l0 {-t}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<path d="M{5 + 2*l + (d-w/3)/2} {5 + yOffset} l0 {t} l{w/3} 0 l0 {-t}" stroke="black" stroke-width="1" fill="none" />'

    sideOutput += '<style type="text/css">.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}.st1{font-family:\'LEMONMILK-Bold\';}.st2{'
    sideOutput += f'font-size:{frontFontSize}px;'
    sideOutput += '}.st3{font-size:7px;}</style>'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/4 + yOffset}" dominant-baseline="middle" text-anchor="middle" class="st2">{frontText}</text>'

    # Side piece bottom screw holes
    sideOutput += f'<circle cx="{5 + l/4}" cy="{yOffset + hp + 2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<circle cx="{5 + 3*l/4}" cy="{yOffset + hp + 2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<circle cx="{5 + l + l/4}" cy="{yOffset + hp+2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<circle cx="{5 + l + 3*l/4}" cy="{yOffset + hp+2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'

    # Facing rights
    sideOutput += f'<path d="M5 {yOffset + 5+ hp/5} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M5 {yOffset + 5 + 4*hp/5} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5 + l} {yOffset + 5 + hp/5} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5 + l} {yOffset + 5 + 4*hp/5} v -1.1 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'

    # Facing lefts
    sideOutput += f'<path d="M{5+l} {yOffset + 5 + hp/5} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+l} {yOffset + 5 + 4*hp/5} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+2*l} {yOffset + 5 + hp/5} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+2*l} {yOffset + 5 + 4*hp/5} v -1.1 h -3 v -1.3 h -1.6 v 1.3 h -1.8 v 2.2 h 1.8 v 1.5 h 1.6 v -1.5 h 3 v -1.1" stroke="black" stroke-width="1" fill="none"/>'

    # Panel holes
    sideOutput += f'<circle cx="{2.4+5+2*l}" cy="{yOffset + 5 + 4*hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+5+2*l}" cy="{yOffset + 5 + hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+0.3+2*l+d}" cy="{yOffset + 5 + 4*hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+0.3+2*l+d}" cy="{yOffset + 5 + hp/5}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{5+2*l+ d/2}" cy="{yOffset + 2.4 + hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'

    # Add SEAS logo + Digital Manufacturing
    sideOutput += f'<g transform="translate({5 + 2*l + d/2 - 11}, {hp/3 + 10 + yOffset}) scale(0.25)">{seas_logo()}</g>'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/3 + 45 + yOffset}" dominant-baseline="middle" text-anchor="middle" class="st3">Digital</text>'
    sideOutput += f'<text x="{5 + 2*l + d/2}" y="{hp/3 + 55 + yOffset}" dominant-baseline="middle" text-anchor="middle" class="st3">Manufacturing</text>'

    return sideOutput

# Generate lid piece path
def Lid():
    # Calculate offsets
    xOffset = 5 + d + t + margin
    yOffset = 5 + L + margin

    lidOutput = f'<path d="M{xOffset} {yOffset} l{w} 0 l0 {l/3} l{t} 0 l0 {l/3} l{-t} 0 l0 {l/3} l{-w/3} 0 l0 {t} l{-w/3} 0 l0 {-t} l{-w/3} 0 l0 {-l/3} l{-t} 0 l0 {-l/3} l{t} 0 l0 {-l/3}" stroke="black" stroke-width="1" fill="none" />'
    lidOutput += f'<circle cx="{xOffset + w/4}" cy="{yOffset + l/4}" r="{w/9}" stroke="black" stroke-width="1" fill="none"/>'
    lidOutput += f'<circle cx="{xOffset + w/2}" cy="{yOffset + l/4}" r="{w/9}" stroke="black" stroke-width="1" fill="none"/>'
    lidOutput += f'<circle cx="{xOffset + 3*w/4}" cy="{yOffset + l/4}" r="{w/9}" stroke="black" stroke-width="1" fill="none"/>'
    lidOutput += f'<rect x="{xOffset + w/4 - w/9}" y="{yOffset + l/2}" width="{w/2 + 2*w/9}" height="{l/3}" rx="3" ry="3" stroke="black" stroke-width="1" fill="none"/>'
    return lidOutput

# Generate fractal pattern
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

# Generate fractal as line path
def generate_fractal():
    depth = random.randint(5,8)
    radius = random.randint(int(r/3), int(r/2))
    center_x = r + 5
    center_y = 3*r/2
    pattern = ""
    for i in range(6):
        angle1 = math.radians(60 * i)
        angle2 = math.radians(60 * (i + 1))
        x1 = center_x + radius * math.cos(angle1)
        y1 = center_y + radius * math.sin(angle1)
        x2 = center_x + radius * math.cos(angle2)
        y2 = center_y + radius * math.sin(angle2)
        pattern += fractal_koch(x1, y1, x2, y2, depth)
    return pattern

# Generate CU SEAS logo as svg path
def seas_logo():
    output = '<g transform="translate(0.000000,870.000000) scale(0.100000,-0.100000)">'
    output += '<path d="M139.2,8666.2c-23.5-16-42.7-29.7-42.4-30.3c0.2-0.8,4-6.5,8.5-12.7l8.1-11.4l42.3,28.6,c23.2,15.8,42.7,29,43.2,29.6c0.7,0.6-14.5,24.1-16.3,25C182.3,8695.1,162.7,8682.2,139.2,8666.2z"/>'
    output += '<path d="M715.4,8673.5c-3.9-6.2-7.2-11.9-7.3-12.8c-0.1-1.1,80-57.5,81.7-57.5c0.6,0,15.9,22.7,15.5,23,c-0.2,0.2-17.7,12.6-38.8,27.5c-21.1,14.9-39.6,28.1-41.1,29.1l-2.8,1.9L715.4,8673.5z"/>'
    output += '<path d="M286.9,8682c-6.4-1.1-17.2-5.3-27.1-10.4c-15.8-8.4-67.7-40.6-169.4-105.4l-35.1-22.5L29.5,8466,c-15-45.4-25.1-77.8-24.5-77.8c0.7,0,37.4-3.7,81.4-8l80.3-8l41.6,26c110.4,68.9,167.7,106.8,178.9,118.3,c11.9,12.3,15.9,29.8,10.9,49c-1,3.5-7.1,13.8-19.9,33c-31.8,47.8-50.4,70.8-62.6,78.1C307.3,8681.5,296.1,8683.6,286.9,8682z"/>'
    output += '<path d="M599.9,8676.3c-8.5-1.5-12.2-3.9-23.1-14.6c-24-24.1-45.7-54.7-63.1-89.3c-8.2-16.1-10.3-25.4-9.4-40.7,c0.7-13.1,1.8-14.7,22.1-33.2c14.7-13.5,35-27.3,80-54.6c82.7-50,141.2-78.6,157.1-76.8c8.2,0.9,19.9,10.1,34.3,27.1,c20,23.5,37.4,50,48.4,73.6c8,17.1,9.2,22.1,9.2,37.5c0,12-0.3,14.1-2.6,18.9c-3.3,6.8-5.4,9.2-16.6,18.5,c-28,23.3-93.9,66.5-163.5,107.3c-34.4,20.2-42.5,23.9-57.9,26.3C607.1,8677.5,606.7,8677.5,599.9,8676.3z"/>' # After this idk what will happen
    output += '<path d="M432.7,8476.9v-14.4l-15.1-0.3l-15.2-0.3l-0.3-17.4l-0.2-17.4l15.1-0.3l15.2-0.3l0.3-15.3l0.3-15.3l-5.6-3.7 c-7.3-4.7-16.5-14.9-19.7-21.8c-5.7-12.7-6-29.9-0.5-41.6c1.7-3.8,5.9-9.9,9.2-13.7c6.5-7.3,6.3-6.5,3.7-16.3 c-1.3-5.1-0.6-4.9-25.4-1.4c-33,4.8-53,9.5-96.5,22.1c-14.1,4.1-30.3,8.5-36.2,9.7c-13.5,2.8-43.3,4-55.9,2.2 c-40.6-5.8-66.4-24.5-73.8-53.5c-4.3-16.4-3.9-51.5,0.4-68.4c4.8-18.3,10-29.4,29.5-62.4c7.5-12.6,15.8-27.6,18.5-33.5 c11.9-25.5,20.4-60.4,22.9-93.7l0.7-10h13.4c30.5-0.1,436.4,4.4,453.2,4.9l18.2,0.6l0.6,15.8c0.9,19.2,3.2,35.7,6.7,46.3 c3.4,10.2,14.6,32.1,25.2,49.1c19.7,31.7,32.3,64.8,36,94.3c1.8,15.1,0.7,36-2.6,49c-7.5,29.2-18.3,46-35.3,54.6 c-5.4,2.7-18.4,6.2-26.2,7.2c-16.6,1.8-67.4-7.2-104.2-18.6c-20.1-6.2-46-12-67.6-15.2c-20-3-47.2-5.1-48.3-3.8 c-0.5,0.5-1.2,3.9-1.6,7.4l-0.6,6.5l4,2.8c4.8,3.3,9.9,10.9,13.1,19.1c3.3,8.6,4,27.6,1.5,35.7c-3.6,11.5-11.7,21.2-22.4,26.9 l-4.8,2.6v16.3v16.4h16h16v17.2v17.1l-15.1,0.3l-15.2,0.3l-0.3,14.3l-0.3,14.2h-15.3h-15.4V8476.9z M261.7,8299.5 c25.9-3.1,50-9.9,68.8-19.4c40.8-20.6,73.4-58.6,83-96.5c3.8-15.6,5.5-61.5,3.2-90c-1.5-18.1-6.5-32-14.6-40.2 c-8.2-8.4-18.5-10.6-35.1-7.7c-18,3.1-27.1,8.2-30.5,16.7c-2.4,5.9-5.2,21.8-4.8,27.2c0.3,4.4,0.4,4.6,4.6,5.4 c2.3,0.4,8.9,0.4,14.7,0.1l10.3-0.6v14.6v14.7h-9.3c-14.9,0-22.4,1.7-27.1,6.3c-4.5,4.2-8,12.8-9,21.9c-0.3,2.9-1.2,5.5-1.8,5.7 c-1.4,0.5-26.6,2.4-27.1,1.9c-0.3-0.3,1.5-18.2,2.8-26.4l0.6-4.1h-16.7H257v-13.3c0-7.3-0.3-14.1-0.6-14.9c-0.5-1.4,2-1.7,17.4-2 c15.7-0.3,18.4-0.6,22.1-2.7c8.4-4.4,12-11,12.9-22.8c1.1-13.7-5.9-21.1-20.7-22.4c-27.7-2.4-57.6,25.6-83.7,77.8 c-9.4,19-27.4,60.3-33.1,76.2c-11.2,30.7-8.5,55.4,7.8,73.6c4.9,5.6,16.1,13.5,23.1,16.6C216.5,8301.2,235.2,8302.6,261.7,8299.5z M682.2,8299c32.4-8.4,51.5-33.5,49.2-64.6c-1-13.1-3.1-21.2-9.8-38.1c-8-20.3-25.7-59.9-33-73.8c-12.7-24.2-28.3-45.4-41.7-56.5 c-21.2-17.8-48.4-20.5-57-5.8c-1.7,2.9-2.2,5.6-2.1,11.8c0,8.7,2,14,7.3,19.6c5.3,5.8,8.2,6.6,26.8,7.1l17.4,0.5v14.8v14.9h-16.5 c-9,0-16.5,0.3-16.5,0.9c0,0.4,0.7,6.8,1.6,14.2c0.9,7.4,1.6,14,1.6,14.5c0,1.1-24.3,0.2-27.3-1c-0.6-0.2-1.5-3-1.9-6 c-1.2-8.5-4.8-17.3-9-21.6c-3.2-3.2-5-4.1-10.9-5.2c-3.8-0.6-11.2-1.2-16.2-1.2h-9.3V8109v-14.6l10.4,0.6 c5.6,0.3,12.2,0.3,14.6-0.1c3.9-0.8,4.3-1.1,4.6-4.7c0.4-5.2-2.4-22-4.7-27.7c-3.4-8.6-12.5-13.7-30.6-16.8 c-26.5-4.6-40.1,4.7-47.8,32.8c-2.1,7.5-2.3,11-2.3,46.9c-0.1,27.6,0.3,41.2,1.4,47.3c4.5,27.1,17.7,51.6,40,74.2 c24.7,24.9,52.7,40.3,88.3,48.4C635.4,8301.2,667.3,8302.8,682.2,8299z"/>'
    output += '<path d="M299,8421.4c-13.4-9-31.9-21.4-41.2-27.5l-16.8-11.1l2.4-4.5c3.7-6.8,15.1-18,25.4-24.8 c22.3-14.8,59.3-28.9,99.7-37.6l11.8-2.6l-14.7,29.7c-19.6,39.7-31.7,66.9-38.4,86.1c-1.3,3.9-2.7,7.3-3.1,7.8 C323.8,8437.3,312.5,8430.3,299,8421.4z"/>'
    output += '<path d="M567.6,8422.5c-3.9-16.1-9-29.7-18.3-48.8c-7.8-16-21.9-38.8-32.3-52.1c-4.5-5.8-5.1-7.1-3.5-7.3 c3.1-0.5,35.5,6.9,51,11.6c41.7,12.8,71.8,30.1,86.1,49.9c3.7,5.2,4.4,6.7,3.3,7.6c-1.1,1-79.3,48.8-82.9,50.6 C570.7,8434.1,569.2,8428.9,567.6,8422.5z"/>'
    output += '<path d="M204.9,7956.5v-21h242.2h242.2v21v21H447.1H204.9V7956.5z"/>'
    output += '<path d="M256.8,7913.8c-1.5-1.9-16.8-22.7-34.1-46.1l-31.4-42.6l47.4-30.5c26.1-16.8,47.7-30.6,48-30.9 c1.5-0.5,14.1,21,30.1,51.9c13.1,24.9,50.9,100,50.9,100.8c0,0.4-24.4,0.8-54.2,0.8h-54.2L256.8,7913.8z"/>'
    output += '<path d="M527.5,7916.7c0-0.3,1.2-2.4,2.6-4.6c4.9-7.8,31.2-59.7,52.8-103.7l21.9-44.9l45.7,29.8 c25.2,16.3,45.9,29.8,46.1,30c0.1,0.1-4.5,7.6-10.2,16.8c-5.9,9.1-16.5,26.7-23.6,39.1c-7.2,12.5-15,26-17.5,30.1l-4.4,7.5 l-56.7,0.3C553,7917.2,527.5,7917.1,527.5,7916.7z"/>'
    output += '</g>'
    return output

# Compile all 
def compile():
    final = starter
    final += Spine()
    final += Base()
    final += Sides()
    final += Lid()
    final += "</svg>"
    f = open('final.svg','w')
    f.write(final)

compile()

