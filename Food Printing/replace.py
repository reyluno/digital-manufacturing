# Open a file named "blinky.gcode"
with open('blinky.gcode', 'r') as file:
    # Read the file line by line
    lines = file.readlines()

# Get user input for the replacement strings
string_0 = input("Enter the string to replace E{EXT_0}: ")
string_1 = input("Enter the string to replace E{EXT_1}: ")

# Replace the strings 'E{EXT_0}' and 'E{EXT_1}' with the user-inputted strings
new_lines = []
for line in lines:
    new_line = line.replace('E{EXT_0}', "E" + string_0)
    new_line = new_line.replace('E{EXT_1}', "E" + string_1)
    new_lines.append(new_line)

# Open a new file called 'test.gcode' in write mode and write the new lines
with open('extruded.gcode', 'w') as file:
    file.writelines(new_lines)
