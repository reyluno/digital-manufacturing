# Base piece code by Nico Aldana and Silvester Nava

d = float(input("Please input an overall depth for the container: ")) #Recommended: 100
L = float(input("Please input an overall length for the container: ")) #Recommended: 125-150


t  = 3.175
dp = d-2*t
r = d/2
l = L - r
            
starter = "<!-- Desk Organizer SVG by Nico Aldana and Silvester Nava c2023 -->\n<!-- Scale: 1:1 pixels to mm -->\n"
starter += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="305" height="457">\n'
output = starter
# Create base outline
output += f'<path d="M5 5 l{dp} 0 l0 {l} l{t} 0 a{r} {r} 0 0 1 {-2*r} 0 l{t} 0 l{0} {-l}" stroke="black" stroke-width="1" fill="none"/>'
# Cut out tab for spine
output += f'<rect x="{5+dp/3}" y="{5+l-t}" width="{dp/3}" height="{t}" stroke="black" stroke-width="1" fill="none"/>'
# End svg
output += '\n</svg>'
f = open('base.svg', 'w')
f.write(output)