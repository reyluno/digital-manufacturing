# Master Desk Organizer Code by Nico Aldana and Silvester Nava

# User inputted variables
d = float(input("Please input an overall depth for the container: ")) #Recommended: 100
L = float(input("Please input an overall length for the container: ")) #Recommended: 125-150
hp = float(input("Please input a height for the pencil holder: ")) # Recommended: 220 - r (> 120)

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
    # Cut out tab for spine
    baseOutput += f'<rect x="{5+dp/3}" y="{5+l}" width="{dp/3}" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
    #Center Screwhole
    baseOutput += f'<path d="M{5+dp/2} 5 v 3 h -1.3 v 1.6 h 1.3 v 1.8 h 2.2 v -1.8 h 1.5 v -1.6 h -1.5 v -3 h -2.2" stroke="black" stroke-width="1" fill="none"/>'
    #Left Screwhole
    baseOutput += f'<path d="M5 {5+0.5*l-1.3} v 1.3 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v 2.2" stroke="black" stroke-width="1" fill="none"/>'
    #Right Screwhole
    baseOutput += f'<path d="M{5+dp-2*t} {5+0.5*l} h 1.8 v -1.3 h 1.6 v 1.3 h 3 v 2.2 h -3 v 1.5 h -1.6 v -1.5 h -1.8 v -2.2" stroke="black" stroke-width="1" fill="none"/>'


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
    spineOutput = output
    spineOutput += f'<path d="M5 {5+r} a{r} {r} 0 0 1 {2*r} 0 l0 {h} l{-(d-dp/3)/2} 0 l0 {t} l{-dp/3} 0 l0 {-t} l{-(d-dp/3)/2} 0 l0 {-h}" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<rect x="{rectX}" y="{rectY}" width="20" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
    # Circle Screwholes
    spineOutput += f'<circle cx="{5+2.4}" cy="{H-0.8*hp+3.2}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{5+2.4}" cy="{H-0.2*hp+3.2}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{H-0.8*hp+3.2}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    spineOutput += f'<circle cx="{2.4+d}" cy="{H-0.2*hp+3.2}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'

    # ADD HOOK PIECE CUTOUT
    #spineOutput += f'<path d="" stroke="black" stroke-width="1" fill="none"/>'

    spineOutput += '\n</svg>'
    f = open('spine.svg', 'w')
    f.write(spineOutput)

def Sides():
    sideOutput = output
    sideOutput += f'<rect x="5" y="5" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + l}" y="5" width="{l}" height="{hp}" stroke="black" stroke-width="1" fill="none" />'
    #Bottom of Side Piece center holes
    sideOutput += f'<circle cx="{5 + 0.5*l}" cy="{hp+2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<circle cx="{5 + 0.5*l + l}" cy="{hp+2.4}" r="1.2" stroke="black" stroke-width="1" fill="none" />'

    #Facing rights
    sideOutput += f'<path d="M5 {5+0.2*hp} v 1.3 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v 2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M5 {5+0.8*hp} v 1.3 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v 2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+l} {5+0.2*hp} v 1.3 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v 2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+l} {5+0.8*hp} v 1.3 h 3 v -1.3 h 1.6 v 1.3 h 1.8 v 2.2 h -1.8 v 1.5 h -1.6 v -1.5 h -3 v 2.2" stroke="black" stroke-width="1" fill="none"/>'    
    
    #Facing lefts
    sideOutput += f'<path d="M{5+l-6.4} {5+0.2*hp+1.3} h 1.8 v -1.3 h 1.6 v 1.3 h 3 v 2.2 h -3 v 1.5 h -1.6 v -1.5 h -1.8 v -2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+l-6.4} {5+0.8*hp+1.3} h 1.8 v -1.3 h 1.6 v 1.3 h 3 v 2.2 h -3 v 1.5 h -1.6 v -1.5 h -1.8 v -2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+2*l-6.4} {5+0.2*hp+1.3} h 1.8 v -1.3 h 1.6 v 1.3 h 3 v 2.2 h -3 v 1.5 h -1.6 v -1.5 h -1.8 v -2.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<path d="M{5+2*l-6.4} {5+0.8*hp+1.3} h 1.8 v -1.3 h 1.6 v 1.3 h 3 v 2.2 h -3 v 1.5 h -1.6 v -1.5 h -1.8 v -2.2" stroke="black" stroke-width="1" fill="none"/>'

    sideOutput += f'<rect x="{5 + 2*l}" y="5" width="{d}" height="{hp}" stroke="black" stroke-width="1" fill="none" />' # Front panel
    #Front Panel Holes
    sideOutput += f'<circle cx="{2.4+5+2*l}" cy="{5+2.4+0.8*hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+5+2*l}" cy="{5+2.4+0.2*hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+0.3+2*l+d}" cy="{5+2.4+0.8*hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{2.4+0.3+2*l+d}" cy="{5+2.4+0.2*hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'
    sideOutput += f'<circle cx="{5+2*l+0.5*d}" cy="{2.4+hp}" r="1.2" stroke="black" stroke-width="1" fill="none"/>'


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


# Create 
Base()
Spine()
Sides()