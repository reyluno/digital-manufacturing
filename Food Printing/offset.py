import sys

def add_x_offset_to_gcode_file(file_path, tool_num, offset):
    """
    Adds a user-specified offset to the X-value of every command in a GCODE file for a specific tool,
    and saves the modified GCODE to a new file called "offset.gcode".

    :param file_path: The path of the GCODE file.
    :type file_path: str
    :param tool_num: The tool number for which to apply the X-offset.
    :type tool_num: int
    :param offset: The X-offset to be applied.
    :type offset: float
    """
    current_tool = None
    with open(file_path, 'r') as f:
        gcode_lines = f.readlines()

    with open('offset.gcode', 'w') as f:
        for line in gcode_lines:
            if line.startswith('T{} '.format(tool_num)):
                current_tool = tool_num
            elif line.startswith('T'):
                current_tool = None

            if current_tool == tool_num:
                tokens = line.strip().split(' ')
                for i, token in enumerate(tokens):
                    if token.startswith('X'):
                        x_value = float(token[1:])
                        x_value += offset
                        tokens[i] = 'X{}'.format(x_value)
                line = ' '.join(tokens) + '\n'

            f.write(line)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python offset.py <file_path> <tool_num> <offset>')
        sys.exit(1)

    file_path = sys.argv[1]
    tool_num = int(sys.argv[2])
    offset = float(sys.argv[3])

    add_x_offset_to_gcode_file(file_path, tool_num, offset)