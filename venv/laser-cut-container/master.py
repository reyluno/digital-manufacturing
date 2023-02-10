# Master Desk Organizer Code by Nico Aldana and Silvester Nava

# User inputted variables
d = float(input("Please input an overall depth for the container: ")) #Recommended: 100
L = float(input("Please input an overall length for the container: ")) #Recommended: 125-150
hp = float(input("Please input a height for the pencil holder: ")) # Recommended: 220 - r

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
    baseOutput += f'<rect x="{5+dp/3}" y="{5+l-t}" width="{dp/3}" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
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
    # ADD CIRCLES FOR SCREW HOLES HERE

    # ADD HOOK PIECE CUTOUT
    #spineOutput += f'<path d="" stroke="black" stroke-width="1" fill="none"/>'

    spineOutput += '\n</svg>'
    f = open('spine.svg', 'w')
    f.write(spineOutput)

def Sides():
    sideOutput = output
    sideOutput += f'<rect x="5" y="5" width="{l}" height="{h}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + l}" y="5" width="{l}" height="{h}" stroke="black" stroke-width="1" fill="none" />'
    sideOutput += f'<rect x="{5 + 2*l}" y="5" width="{d}" height="{h}" stroke="black" stroke-width="1" fill="none" />' # Front panel

    # ADD CIRCLES AND SCREW CONTOURS

    sideOutput += '\n</svg>'
    f = open('sides.svg', 'w')
    f.write(sideOutput)


# Create 
Base()
Spine()
Sides()