def sierpinski_triangle(n, x=0, y=0):
    svg_header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%"
xmlns="http://www.w3.org/2000/svg">"""

    svg_footer = "</svg>"

    svg_elements = []

    def recursive_triangle(points, depth):
        if depth == 0:
            x1, y1 = points[0]
            x2, y2 = points[1]
            x3, y3 = points[2]
            svg_elements.append(f'<polygon points="{x1},{-y1} {x2},{-y2} {x3},{-y3}" fill="black"/>')
        else:
            x1, y1 = points[0]
            x2, y2 = points[1]
            x3, y3 = points[2]
            x12 = (x1 + x2) / 2
            y12 = (y1 + y2) / 2
            x23 = (x2 + x3) / 2
            y23 = (y2 + y3) / 2
            x31 = (x3 + x1) / 2
            y31 = (y3 + y1) / 2
            recursive_triangle([(x1, y1), (x12, y12), (x31, y31)], depth - 1)
            recursive_triangle([(x12, y12), (x2, y2), (x23, y23)], depth - 1)
            recursive_triangle([(x31, y31), (x23, y23), (x3, y3)], depth - 1)

    size = 2**n
    x1 = x
    y1 = y
    x2 = x + size
    y2 = y
    x3 = x + size / 2
    y3 = y + (3**0.5) / 2 * size
    x_offset = -size / 2
    y_offset = -y3 / 2
    recursive_triangle([(x1 + x_offset, y1 + y_offset), (x2 + x_offset, y2 + y_offset), (x3 + x_offset, y3 + y_offset)], n)

    return svg_header + '\n'.join(svg_elements) + svg_footer

f = open('triangle.svg','w')
f.write(sierpinski_triangle(5, 10, -10))
