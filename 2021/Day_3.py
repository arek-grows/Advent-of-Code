def part_one(data_input):
    gamma = ""
    epsilon = ""
    # two lists to count number of 0s and 1s in each index
    zeroes = [0 for xx in range(len(data_input[0]))]
    ones = [0 for xx in range(len(data_input[0]))]

    for binary_num in data_input:
        for ii, bit in zip(range(len(binary_num)), binary_num):
            if bit == '0':
                zeroes[ii] += 1
            elif bit == '1':
                ones[ii] += 1
            else:
                return 'error: not a 0 or 1'

    for zero, one in zip(zeroes, ones):
        if zero > one:
            gamma += "0"
            epsilon += "1"
        elif one > zero:
            gamma += "1"
            epsilon += "0"
        else:
            return "error: number of ones and zeroes is equal"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def part_two(data_input):
    bin_length = len(data_input[0])
    possible_oxygen = data_input.copy()
    possible_C02 = data_input.copy()

    # oxygen generator rating
    for ii in range(bin_length):
        zeroes = 0
        ones = 0
        zeroes_list = []
        ones_list = []
        for bin_value in possible_oxygen:
            if bin_value[ii] == "0":
                zeroes += 1
                zeroes_list.append(bin_value)
            elif bin_value[ii] == "1":
                ones += 1
                ones_list.append(bin_value)
            else:
                return 'error: not a 0 or 1'
        if zeroes > ones:
            possible_oxygen = zeroes_list
        elif ones > zeroes or ones == zeroes:
            possible_oxygen = ones_list

        if len(possible_oxygen) == 1:
            break

    if len(possible_oxygen) != 1:
        return 'error: oxygen generator rating not found'
    oxygen_generator_rating = int(possible_oxygen[0], 2)

    # C02 scrubber rating
    for ii in range(bin_length):
        zeroes = 0
        ones = 0
        zeroes_list = []
        ones_list = []
        for bin_value in possible_C02:
            if bin_value[ii] == "0":
                zeroes += 1
                zeroes_list.append(bin_value)
            elif bin_value[ii] == "1":
                ones += 1
                ones_list.append(bin_value)
            else:
                return 'error: not a 0 or 1'
        if zeroes < ones or zeroes == ones:
            possible_C02 = zeroes_list
        elif ones < zeroes:
            possible_C02 = ones_list

        if len(possible_C02) == 1:
            break

    if len(possible_C02) != 1:
        return 'error: C02 scrubber rating not found'
    C02_scrubber_rating = int(possible_C02[0], 2)

    return oxygen_generator_rating * C02_scrubber_rating


input_file = open(r"C:\Users\arkad\Desktop\Advent of Code\AoC_day_3_input.txt", "r")
data = input_file.read().split("\n")
example_data = ["00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010"]

print(part_one(example_data))
print(part_one(data))
print(part_two(example_data))
print(part_two(data))
