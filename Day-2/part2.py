
'''
    A for Rock, B for Paper, and C for Scissors

    X for Rock, Y for Paper, and Z for Scissors

    A Y
    B X
    C Z
'''
oponet_score = 0
player_score = 0

oponent = {
    'A':[1,'Y','Z','X'],
    'B':[2,'Z','X','Y'],
    'C':[3,'X','Y','Z']

}

player = {
    'X':[1,'B','C'],
    'Y':[2,'C','A'],
    'Z':[3,'A','B']
}

with open('list.text') as l:
    lines = l.readlines()


for line in lines:
    op = line[0]
    pl = line[2]

    if pl == 'X':
        pl = oponent[op][2]
    elif pl == 'Y':
        pl = oponent[op][3]
    else:
        pl = oponent[op][1]

    # If are de same value
    if oponent[op][0] == player[pl][0]:
        oponet_score = oponet_score + 3 + oponent[op][0]
        player_score = player_score + 3 + player[pl][0]
    else:
        if oponent[op][1] == pl:
            player_score = player_score + 6 + player[pl][0]
            oponet_score = oponet_score + 0 + oponent[op][0]
        elif oponent[op][2] == pl:
            oponet_score = oponet_score + 6 + oponent[op][0]
            player_score = player_score + 0 + player[pl][0]

print(f'Oponet Score: {oponet_score}')
print(f'Player Score: {player_score}')