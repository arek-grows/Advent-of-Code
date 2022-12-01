def part_one(coords, is_p_two):
    points_covered = dict()
    for line_coord in coords:
        end_a = line_coord[0].split(",")
        end_b = line_coord[1].split(",")
        xs = [int(end_a[0]), int(end_b[0])]
        ys = [int(end_a[1]), int(end_b[1])]
        if xs[0] == xs[1]:
            low, high = min(ys), max(ys)
            for yy in range(low, high + 1):
                coord_string = f"{xs[0]},{yy}"
                if coord_string not in points_covered:
                    points_covered[coord_string] = 0
                points_covered[coord_string] += 1
        elif ys[0] == ys[1]:
            low, high = min(xs), max(xs)
            for xx in range(low, high + 1):
                coord_string = f"{xx},{ys[0]}"
                if coord_string not in points_covered:
                    points_covered[coord_string] = 0
                points_covered[coord_string] += 1
        elif is_p_two:
            x_slope = 1
            if xs[0] > xs[1]:
                x_slope = -1
            y_slope = 1
            if ys[0] > ys[1]:
                y_slope = -1
            # print(f"[{xs[0]}, {ys[0]}] -> [{xs[1]} -> {ys[1]}]")
            for xx, yy in zip(range(xs[0], xs[1] + x_slope, x_slope), range(ys[0], ys[1] + y_slope, y_slope)):
                coord_string = f"{xx},{yy}"
                if coord_string not in points_covered:
                    points_covered[coord_string] = 0
                points_covered[coord_string] += 1

    line_overlaps = 0
    for cc in points_covered:
        if points_covered[cc] >= 2:
            line_overlaps += 1
    return line_overlaps


input_file = open(r"C:\Users\arkad\Desktop\Advent of Code\Aoc_day_5_input.txt", "r")
# input_file = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""

input_data = input_file.read().split("\n")
line_coords = []
[line_coords.append(aa.split(" -> ")) for aa in input_data]
# [print(dd) for dd in line_coords]

is_part_two = True
print(part_one(line_coords, is_part_two))
