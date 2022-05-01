import os

def main():

    # Read file lines
    script_dir = os.path.dirname(__file__)
    rel_path = "\input.txt"
    abs_file_path = script_dir + rel_path

    increases = 0
    decreases = 0
    previous_depth = 0
    current_depth = 0

    with open(abs_file_path, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()

            # set previous and current depths
            previous_depth = current_depth
            current_depth = int(stripped_line)

            # count number of changes
            if current_depth > previous_depth:
                increases += 1
            elif current_depth < previous_depth:
                decreases += 1

        print(increases-1, decreases)

if __name__ == "__main__":
    main()
