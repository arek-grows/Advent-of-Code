import math

input_file = open("day8input.txt", 'r')
input_raw = input_file.read()
input_file.close()
raw_list = input_raw.split('\n')
pre_string_list = []

# pre_string[0] holds the first line of input
# pre_string[0][0] hold the mixed letters
# pre_string[0][1] holds the mixed output
for x, a in enumerate(raw_list):
    pre_string_list.append(a.split(' | '))
    pre_string_list[x][0] = pre_string_list[x][0].split()
    pre_string_list[x][1] = pre_string_list[x][1].split()

total = 0

for inputs in pre_string_list:
    cyp_dct = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': ''}
    let_dct = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    five_list = []
    six_list = []
    for jumbled in inputs[0]:
        ln = len(jumbled)
        if ln == 6:
            six_list.append(jumbled)
        elif ln == 5:
            five_list.append(jumbled)
        elif ln == 2:
            let_dct[1] = jumbled
        elif ln == 3:
            let_dct[7] = jumbled
        elif ln == 4:
            let_dct[4] = jumbled
        elif ln == 7:
            let_dct[8] = jumbled
    d_c_or_e = ""
    for sixer in six_list:
        for ss in sixer:
            if ss not in let_dct[8]:
                d_c_or_e += ss
    for let in d_c_or_e:
        if let in let_dct[1]:
            cyp_dct['c'] = let
            break
