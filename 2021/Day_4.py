def check_win(matrix_board):
    for row in matrix_board:
        if all(row):
            return True
    # columns
    for kk in range(5):
        if all([row[kk] for row in matrix_board]):
            return True
    return False


def create_number_location_dict(game_boards):
    location_dict = {}
    for board_index, board in enumerate(game_boards):
        for row_index, row in enumerate(board):
            for nr_index, nr in enumerate(row):
                if nr not in location_dict:
                    location_dict[nr] = []
                location_dict[nr].append([board_index, row_index, nr_index])
    return location_dict


def part_one(drawn_numbers, game_boards, nr_locations):
    # matrix of equal size to game_boards to keep track of marked numbers
    matching_matrix = []
    [matching_matrix.append([[False for ab in range(5)] for cd in range(5)]) for nrgb in range(len(game_boards))]

    winning_board_index = -1
    winning_number = -1
    won_boards = []
    for first_four in drawn_numbers[0:4]:
        for iis in nr_locations[first_four]:
            matching_matrix[iis[0]][iis[1]][iis[2]] = True
    for rest_nrs in drawn_numbers[4:]:
        # is_win = False
        for iis in nr_locations[rest_nrs]:
            board_number = iis[0]
            if board_number not in won_boards:
                matching_matrix[iis[0]][iis[1]][iis[2]] = True
                is_win = check_win(matching_matrix[board_number])
                if is_win:
                    winning_board_index = board_number
                    winning_number = rest_nrs
                    won_boards.append(board_number)
        # uncomment these 4 lines to have a working solution for part one, recomment for part 2
        #         is_win = True
        #         break
        # if is_win:
        #     break

    winning_board = game_boards[winning_board_index]
    winning_matrix = matching_matrix[winning_board_index]
    unmarked_total = 0
    for b_row, m_row in zip(winning_board, winning_matrix):
        for b_nr, m_is in zip(b_row, m_row):
            if not m_is:
                unmarked_total += b_nr
    return unmarked_total * winning_number


# example data
# input_file = open(r"C:\Users\arkad\Desktop\Advent of Code\Day_4_example_data.txt", "r")
# input_data = input_file.read().split("\n")
# actual data
input_file = open(r"C:\Users\arkad\Desktop\Advent of Code\Aoc_day_4_input.txt", "r")
input_data = input_file.read().split("\n")

number_draw = input_data[0].split(",")
number_draw = [int(num) for num in number_draw]

# 3d list containing multiple bingo boards. i[0] = board, i[0][0] = row, i[0][0][0] = number
bingo_boards = []
for ii in range(2, len(input_data) - 4, 6):
    bingo_board = []
    for xx in range(ii, ii + 5):
        row = input_data[xx].split()
        bingo_board.append([int(num) for num in row])
    bingo_boards.append(bingo_board)

# dictionary that points to the index of where specific numbers are located on the game boards
location_dict = create_number_location_dict(bingo_boards)

# print(number_draw)
# for bb in bingo_boards:
#     for BB in bb:
#         print(BB)
#     print("\n")

print(part_one(number_draw, bingo_boards, location_dict))
