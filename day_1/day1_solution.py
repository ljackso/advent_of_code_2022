
input_file_name = 'day1_input.txt'

def main():
    file = open(input_file_name, "r")
    elf_calories = []
    cum_cal = 0
    for line in file:
        cal_raw = line[:len(line) - 1]
        if cal_raw == '':
            elf_calories.append(cum_cal)
            cum_cal = 0
        else :
            cum_cal += int(cal_raw)

    part1_answer = max(elf_calories)
    part2_answer = sum(sorted(elf_calories, reverse = True)[:3])

    print('Part 1 = ' + part1_answer)
    print('Part 2 = ' + part2_answer)

if __name__ == "__main__":
    main()
