
input_file_name = 'day2_input.txt'

def main():
    file = open(input_file_name, "r")

    p1_rps_dict = {
        'A':'Rock',
        'X':'Rock',
        'B':'Paper',
        'Y':'Paper',
        'C':'Scissors',
        'Z':'Scissors'
    }

    p2_inst_dict = {'X':'Lose','Y':'Draw','Z':'Win'}

    rps_score_dict = {'Rock':1,'Paper': 2,'Scissors':3}
    score_dict = {'Lose':0, 'Draw': 3,'Win':6}

    part1_answer = 0
    part2_answer = 0
    for line in file:
        line_raw = line[:len(line) - 1]
        part1_answer += (score_dict[play_rps(p1_rps_dict[line_raw[0]],p1_rps_dict[line_raw[2]])] + rps_score_dict[p1_rps_dict[line_raw[2]]])
        part2_answer += (rps_score_dict[target_move(p1_rps_dict[line_raw[0]],p2_inst_dict[line_raw[2]])] + score_dict[p2_inst_dict[line_raw[2]]])

    print('Part 1 = ' + str(part1_answer))
    print('Part 2 = ' + str(part2_answer))

def target_move(opponent, outcome):
    if outcome == 'Draw':
        return opponent
    elif outcome == 'Win':
        if opponent == 'Rock':
            return 'Paper'
        elif opponent == 'Paper':
            return 'Scissors'
        elif opponent == 'Scissors':
            return 'Rock'
    elif outcome == 'Lose':
        if opponent == 'Rock':
            return 'Scissors'
        elif opponent == 'Paper':
            return 'Rock'
        elif opponent == 'Scissors':
            return 'Paper'

def play_rps(opponent, player):
    if opponent == player:
        return 'Draw'
    elif player == 'Rock':
        if opponent == 'Scissors':
            return 'Win'
        elif opponent == 'Paper':
            return 'Lose'
    elif player == 'Paper':
        if opponent == 'Rock':
            return 'Win'
        elif opponent == 'Scissors':
            return 'Lose'
    elif player == 'Scissors':
        if opponent == 'Paper':
            return 'Win'
        elif opponent == 'Rock':
            return 'Lose'


if __name__ == "__main__":
    main()
