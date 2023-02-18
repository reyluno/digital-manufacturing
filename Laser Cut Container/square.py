side = float(input("Please enter a side length for the square: "))
content = input("Please enter your initials: ")

output = '<?xml version="1.0" encoding="utf-8"?><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"><style type="text/css">.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}.st1{font-family:\'LEMONMILK-Bold\';}.st2{font-size:30px;}</style><rect class="st0" x="0" y="0" width="%f" height="%f"/><text x="%f" y="%f" dominant-baseline="middle" text-anchor="middle" class="st1 st2">%s</text></svg>' % (side, side, side/2, side/2, content)

f = open('square.svg', 'w')
f.write(output)

