import os

def main():

    # Read file lines
    script_dir = os.path.dirname(__file__)
    rel_path = "\input.txt"
    abs_file_path = script_dir + rel_path

    depth_array = []
    increases = 0
    decreases = 0
    previous_depth_window = 0

    # add depths to array to iterate through
    with open(abs_file_path, "r") as a_file:
        for line in a_file:
            stripped_line = int(line.strip())
            depth_array.append(stripped_line)

    # calculate differences of the windows
    for i in range(len(depth_array)-2):
        current_depth_window = 0
        for j in range(3):
            current_depth_window += depth_array[i+j]
        if current_depth_window > previous_depth_window:
            increases += 1
        elif current_depth_window < previous_depth_window:
            decreases += 1
        previous_depth_window = current_depth_window

    print(increases-1, decreases)


if __name__ == "__main__":
    main()
