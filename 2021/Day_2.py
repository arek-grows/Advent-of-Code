def part_one(data_input):
    horizontal = 0
    depth = 0

    for direction in data_input:
        dd = direction.split()
        command = dd[0]
        distance = int(dd[1])
        if command == "forward":
            horizontal += distance
        elif command == "down":
            depth += distance
        elif command == "up":
            depth -= distance
        else:
            return "error"

    return horizontal * depth


def part_two(data_input):
    horizontal = 0
    depth = 0
    aim = 0

    for direction in data_input:
        dd = direction.split()
        command = dd[0]
        distance = int(dd[1])
        if command == "forward":
            horizontal += distance
            depth += aim * distance
        elif command == "down":
            aim += distance
        elif command == "up":
            aim -= distance
        else:
            return "error"

    return horizontal * depth


input_file = open(r"C:\Users\arkad\Desktop\Advent of Code\Aoc_day_2_input.txt", "r")
data = input_file.read().split("\n")

print(part_one(data))
print(part_two(data))
