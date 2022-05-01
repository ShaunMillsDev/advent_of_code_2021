import os

# main method
def main():

    # get input as array
    diagnostic_report = get_file_array()

    # initialise array with 0's based on length of binary strings in diagnostic report array
    result = [0 for i in range(len(diagnostic_report[0]))]
    gamma_rate = ""
    epsilon_rate = ""

    # increase or decrease result[] values by 1 depending on the binary string value
    for binary_string in diagnostic_report:
        for i in range(len(binary_string)):
            if binary_string[i] == '1':
                result[i] += 1
            else:
                result[i] -= 1

    # convert resulting array of values to a binary string
    for i in range(len(result)):
        if result[i] > 0:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    # convert binary string to integers and multiply together
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)

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
