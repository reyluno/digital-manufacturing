# @Title: calibration.py
# @Description: g-code generator for food printer that determines the best feedrate/extrusion
# @Author: Nico Aldana

import argparse

BASE_FEEDRATE = 200 # mm/min
BASE_EXTRUSION = 0.5 # mm/min
DEFAULT_LENGTH = 50
BUFFER = 5
E_INCREMENT = 0.1
num_lines = 5

def main(length):
    lines = []
    eol = "\n"
    lines.append("T0" + eol)  # Select extruder 0
    lines.append("G21"+ eol) # Set units to mm
    lines.append("G92 X0 Y0 Z0 E0" + eol) # Set current position to be the origin
    lines.append("G91" + eol) # Send relative position commands
    lines.append(f"G1 E0.25" + eol) # Prime the nozzle

    for i in range(0, num_lines):
        lines.append(f"G1 X{length} E{BASE_EXTRUSION + (i*E_INCREMENT)} F{BASE_FEEDRATE}" + eol) # Draw line
        lines.append(f"G1 Z5") # Raise the nozzle slightly
        lines.append(f"G0 X{-length} Y{BUFFER} Z0" + eol) # Move over to the next line

    lines.append(f"G1 X{length} Y{BUFFER} Z0 E{BASE_EXTRUSION + E_INCREMENT} + F{BASE_FEEDRATE}") # Line 2
    lines.append(f"G1 Z5") # Raise the nozzle slightly
    lines.append(f"G0 X0 Y{2*BUFFER} Z0" + eol) # Move over to the next line
    lines.append(f"G1 X{length} Y{BUFFER} Z0 E{BASE_EXTRUSION + E_INCREMENT} + F{BASE_FEEDRATE}") # Line 2

    lines.append("G1 Z5 E-2 F200" + eol) # move up & retract plunger a bit
    lines.append("G1 X0 Y0 F400 " + eol) # move away from the print and go to origin
    lines.append("G28") # Home printer
    # write lines to file
    with open('calibration.gcode', 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create G-Code for calibration')
    parser.add_argument('side_length', metavar='l', nargs='?', type=int, default = DEFAULT_LENGTH,
                        help='Pass an integer for side length in mm')

    args = parser.parse_args()
    main(args.side_length)