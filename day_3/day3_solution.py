input_file_name = 'day3_input.txt'

def main():
    file = open(input_file_name).read().splitlines()

    p1, p2, count = 0, 0, 0
    for line in file:
        p1 += get_prio(get_matches(line[:len(line)//2], line[len(line)//2:])[0])
        if not count % 3: p2 += get_prio(get_matches(get_matches(line, file[count+1]), file[count+2])[0])
        count += 1

    print('Part 1 = ' + str(p1))
    print('Part 2 = ' + str(p2))

def get_matches(s1, s2):
    return [i for i in s1 if i in s2]

def get_prio(char):
    if char.isupper(): return ord(char.lower()) - 70
    return ord(char) - 96

if __name__ == "__main__":
    main()
