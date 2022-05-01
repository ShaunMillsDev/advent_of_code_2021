import os

# main method
def main():

    instructions = get_file_array()

    horizontal_position = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        instruction_split = instruction.split(" ")
        direction = instruction_split[0]
        value = int(instruction_split[1])

        if direction == "forward":
            horizontal_position += value
            depth += aim * value
        elif direction == "down":
            aim += value
        else:
            aim -= value

    final_value = horizontal_position * depth

    print("Horizontal: " + str(horizontal_position))
    print("Depth: " + str(depth))
    print("Final value: " + str(final_value))


# turns file input into array for easier processing
def get_file_array():
    file_array = []

    # Read file lines
    script_dir = os.path.dirname(__file__)
    rel_path = "\input.txt"
    abs_file_path = script_dir + rel_path

    # add lines to array to iterate through
    with open(abs_file_path, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            file_array.append(stripped_line)

    return file_array


# program entry point
if __name__ == "__main__":
    main()
