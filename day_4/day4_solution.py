input_file_name = 'day4_input.txt'

def main():
    file = open(input_file_name).read().splitlines()

    p1, p2 = 0, 0
    for line in file:
        e1_ids = [int(i) for i in  line.split(',')[0].split('-')]
        e2_ids = [int(i) for i in  line.split(',')[1].split('-')]

        if e1_ids[0] <= e2_ids[0] <= e1_ids[1] and e1_ids[0] <= e2_ids[1] <= e1_ids[1]: p1 += 1
        elif e2_ids[0] <= e1_ids[0] <= e2_ids[1] and e2_ids[0] <= e1_ids[1] <= e2_ids[1]: p1 += 1

        if e1_ids[0] <= e2_ids[0] <= e1_ids[1] or e1_ids[0] <= e2_ids[1] <= e1_ids[1]: p2 += 1
        elif e2_ids[0] <= e1_ids[0] <= e2_ids[1] or e2_ids[0] <= e1_ids[1] <= e2_ids[1]: p2 += 1


    print('Part 1 = ' + str(p1))
    print('Part 2 = ' + str(p2))

if __name__ == "__main__":
    main()
