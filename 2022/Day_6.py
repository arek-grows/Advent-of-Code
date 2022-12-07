def tuner_searcher(inp_dt, looking_for):
    marker_location = None
    search_num = 4
    if looking_for not in ["packet", "message"]:
        print("invalid parameter in tuner_search()")
        return marker_location
    elif looking_for == "message":
        search_num = 14

    for idx in range(0, len(inp_dt)):
        potential_marker = inp_dt[idx:idx + search_num]
        if len(set(potential_marker)) == len(potential_marker):
            marker_location = idx + search_num
            break
    return marker_location


if __name__ == "__main__":

    sample_input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg"]

    with open("data/day_6_input.txt") as input_file:
        input_data = input_file.read()

    # for ss in sample_input:
    #     print(tuner_searcher(ss, "message"))
    print(tuner_searcher(input_data, "message"))
