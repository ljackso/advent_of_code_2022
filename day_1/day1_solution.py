
input_file_name = 'day1_input.txt'

def main():
    file = open(input_file_name).read().splitlines()

    elf_calories = []
    cum_cal = 0
    for line in file:
        if line == '':
            elf_calories.append(cum_cal)
            cum_cal = 0
        else:
            cum_cal += int(line)

    p1 = max(elf_calories)
    p2 = sum(sorted(elf_calories, reverse = True)[:3])

    print('Part 1 = ' + str(p1))
    print('Part 2 = ' + str(p2))

if __name__ == "__main__":
    main()
