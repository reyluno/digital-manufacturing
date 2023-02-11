import math

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

if __name__ == '__main__':
    center_x = 200
    center_y = 200
    radius = 100
    pattern = ""
    for i in range(6):
        angle1 = math.radians(60 * i)
        angle2 = math.radians(60 * (i + 1))
        x1 = center_x + radius * math.cos(angle1)
        y1 = center_y + radius * math.sin(angle1)
        x2 = center_x + radius * math.cos(angle2)
        y2 = center_y + radius * math.sin(angle2)
        pattern += fractal_koch(x1, y1, x2, y2, 5)
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>{pattern}</svg>"
    f = open('snowflake.svg','w')
    f.write(svg)