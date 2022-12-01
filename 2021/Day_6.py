# fish_list = []
#
#
# class Lanternfish:
#     def __init__(self, breed_date=8):
#         self.breed_date = breed_date
#
#     global fish_list
#
#     def day_pass(self):
#         if self.breed_date == 0:
#             fish_list.append(Lanternfish())
#             self.breed_date = 6
#         else:
#             self.breed_date -= 1
#
#
# def part_one(input_fish, nr_days):
#     global fish_list
#     for ff in input_fish:
#         fish_list.append(Lanternfish(ff))
#     for day in range(nr_days):
#         for fish in fish_list[0:len(fish_list)]:
#             fish.day_pass()
#     return len(fish_list)
#
#
# def part_one(input_fish, nr_days):
#     for day in range(nr_days):
#         for ii, fish in enumerate(input_fish[0:len(input_fish)]):
#             if fish != 0:
#                 input_fish[ii] -= 1
#             else:
#                 input_fish[ii] = 6
#                 input_fish.append(8)
#         print(f"day {day + 1} fish: {len(input_fish)}")
#     return len(input_fish)


def part_one(input_fish, nr_days):
    # index 0 is after 1 day
    birth_calendar = [0 for xx in range(0, nr_days)]
    fish_set = set(input_fish)
    for parent in fish_set:
        fish_count = input_fish.count(parent)
        for dd in range(parent, nr_days, 7):
            birth_calendar[dd] += fish_count
    for ii, births in enumerate(birth_calendar):
        if ii + 9 <= nr_days - 1:
            birth_calendar[ii + 9] += births
            for dd in range(ii + 9 + 7, nr_days, 7):
                birth_calendar[dd] += births
    return len(input_fish) + sum(birth_calendar)


input_data = open(r"C:\Users\arkad\Desktop\Advent of Code\Aoc_day_6_input.txt", "r")
# input_data = "3,4,3,1,2"

input_data = input_data.read().split(",")
fish_days = [int(uu) for uu in input_data]
days_to_pass = 256

print(part_one(fish_days, days_to_pass))
