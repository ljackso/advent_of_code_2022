input_file_name = 'day6_input.txt'

def main():
    input_str = open(input_file_name).read().splitlines()[0]
    print('Part 1 = ' + str(get_dis_lis_pos(input_str, 4)))
    print('Part 2 = ' + str(get_dis_lis_pos(input_str, 14)))

def get_dis_lis_pos(input, d_len):
    temp_list = []
    for index, char in enumerate(input):
        if char not in temp_list:
            temp_list.append(char)
            if len(temp_list) == d_len:
                return index + 1
        else:
            temp_list = [x for x in ''.join(temp_list).split(char)[1]]
            temp_list.append(char)

if __name__ == "__main__":
    main()
