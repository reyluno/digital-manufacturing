import struct

# Define the size of the square in centimeters
width = 5
height = 5

# Define the size of each stitch in millimeters
stitch_size = 1

# Define the number of stitches in each direction
num_stitches_x = int(width * 10 / stitch_size)
num_stitches_y = int(height * 10 / stitch_size)

# Define the starting point of the embroidery pattern
start_x = -num_stitches_x // 2
start_y = -num_stitches_y // 2

# Create a list to hold the stitches
stitches = []

# Loop through each stitch and append the delta x and delta y values to the list
for i in range(num_stitches_x):
    for j in range(num_stitches_y):
        delta_x = stitch_size
        delta_y = 0
        if j % 2 == 0:
            delta_y = stitch_size
        stitches.append((start_x + i * stitch_size / 10, start_y + j * stitch_size / 10, delta_x / 10, delta_y / 10))

# Create the header data
header_data = struct.pack('<6sHH', b'JEF', 512, 512)

# Convert the stitches to bytes for a .jef embroidery file
embroidery_data = b''
for stitch in stitches:
    embroidery_data += struct.pack('<hh', int(stitch[2] * 1000), int(stitch[3] * 1000))

# Write the embroidery data to a file
with open('square.jef', 'wb') as f:
    f.write(header_data)
    f.write(embroidery_data)
