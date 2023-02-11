import math

def fractal_tree(x1, y1, angle, depth, size):
    if depth == 0:
        return ""
    x2 = x1 + math.cos(math.radians(angle)) * depth * 5.0
    y2 = y1 + math.sin(math.radians(angle)) * depth * 5.0
    result = f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='black' stroke-width='{size}' />"
    result += fractal_tree(x2, y2, angle - 20, depth - 1, size * 0.8)
    result += fractal_tree(x2, y2, angle + 20, depth - 1, size * 0.8)
    return result

if __name__ == '__main__':
    pattern = fractal_tree(400, 700, -90, 7, 6) #-90, 9, 5
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' width='800' height='1000'>{pattern}</svg>"

    f = open('fractal.svg','w')
    f.write(svg)
