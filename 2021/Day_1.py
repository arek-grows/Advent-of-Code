input_file_1 = open(r"C:\Users\arkad\Desktop\AoC_day_1_input_1.txt", "r")

pre_input = input_file_1.read().split('\n')
pre_input = [int(xx) for xx in pre_input]
# pre_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
puzzle_input = []

for ii in range(len(pre_input) - 2):
    puzzle_input.append(pre_input[ii] + pre_input[ii + 1] + pre_input[ii + 2])

previous = puzzle_input[0]
increased = 0

for pp in puzzle_input[1:]:
    if pp > previous:
        increased += 1
    previous = pp

print(increased)
