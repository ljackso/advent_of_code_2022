input_file_name = 'day5_input.txt'

def main():
    file = open(input_file_name).read().splitlines()

    stack = []
    index, end = 0, 0
    for line in file:
        if line == '':
            for i in range(0,int(file[index -1][-1])):
                stack.append([])
                end = index - 2
            break
        index += 1

    entry_len = (len(stack) * 4) - 1
    row = 0
    for line in file:
        if row <= end:
            for i in range(0,len(line)):
                if not (i-1) % 4 and line[i] != ' ':
                    stack[(i-1)//4].insert(0,line[i])
        elif row > (end+2):
            instr = line.split(' ')
            q, pos1, pos2 = int(instr[1]),int(instr[3])-1,int(instr[5])-1
            temp_stack = stack[pos1][-q:]
            #temp_stack.reverse()  #uncomment for part 1
            stack[pos1] = stack[pos1][:len(stack[pos1])-q]
            stack[pos2] = stack[pos2] + temp_stack
        row += 1

    answ = []
    for l in stack:
        if len(l) > 0: answ.append(l[len(l)-1])

    print('Answer = ' + ''.join(answ))

if __name__ == "__main__":
    main()
