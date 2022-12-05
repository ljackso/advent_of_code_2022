input_file_name = 'day5_input.txt'

def main():
    file = open(input_file_name).read().splitlines()

    stack = []
    end = 0
    for index, line in enumerate(file):
        if line == '':
            for i in range(0,int(file[index-1][-1])):
                stack.append([])
                end = index - 2
            break

    entry_len = (len(stack) * 4) - 1
    for index, line in enumerate(file):
        if index <= end:
            for i in range(0,len(line)):
                if not (i - 1) % 4 and line[i] != ' ':
                    stack[(i-1)//4].insert(0,line[i])
        elif index > (end + 2):
            instr = line.split(' ')
            q, pos1, pos2 = int(instr[1]),int(instr[3])-1,int(instr[5])-1
            temp_stack = stack[pos1][-q:]
            #temp_stack.reverse()  #uncomment for part 1
            stack[pos1] = stack[pos1][:len(stack[pos1])-q]
            stack[pos2] = stack[pos2] + temp_stack

    print('Answer = ' + ''.join([l[-1] for l in stack]))

if __name__ == "__main__":
    main()
