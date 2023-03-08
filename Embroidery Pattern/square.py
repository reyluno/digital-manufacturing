# Embroidery Pattern Test File by Nico Aldana & Silvester Nava

stitches = [128, 2,
            0, 0,
            206, 206,]

# Make a 5x5 square
for i in range(0,10):
    stitches += [10, 0,]
for i in range(0,10):
    stitches += [0, 10,]
for i in range(0,10):
    stitches += [246, 0,]
for i in range(0,10):
    stitches += [0, 246,]

stitches += [128, 16] # Last stitch command

jefBytes = [124, 0, 0, 0, # Byte offset of the first stitch
            10, 0, 0, 0, # Unknown number
            ord("2"), ord("0"), ord("2"), ord("3"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("2"), # MMDD
            ord("1"), ord("6"), ord("2"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0, # SS00
            1, 0, 0, 0, # Number of physical threads (1)
            (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0, # Number of stitches
            3, 0, 0, 0, # Sewing machine hoop
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0, # Bottom boundary distance from center (in 0.1 mm)
            1, 0, 0, 0, # Thread color (2 = White)
            13, 0, 0, 0, # Unknown number
            ] + stitches

print(jefBytes)
jefBytes = bytes(jefBytes)
with open("testsquare.jef", "wb") as f:
    f.write(jefBytes)