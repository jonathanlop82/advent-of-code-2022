import re

num_of_staks = 9

staks = {
    1:['J','H','P','M','S','F','N','V'],
    2:['S','R','L','M','J','D','Q'],
    3:['N','Q','D','H','C','S','W','B'],
    4:['R','S','C','L'],
    5:['M','V','T','P','F','B'],
    6:['T','R','Q','N','C'],
    7:['G','V','R'],
    8:['C','Z','S','P','D','L','R'],
    9:['D','S','J','V','G','P','B','F']
}

staks1 = {
    1:['Z','N'],
    2:['M','C','D'],
    3:['P']
}

def print_staks():
    for i in range(num_of_staks):
        print(staks[i+1])

with open('list.text') as l:
    lines = l.readlines()

number_regex = re.compile('\d{1,2}')
moves = []
for line in lines:
    line = line.replace('\n','')
    first = number_regex.findall(line)
    res= [eval(i) for i in first]
    moves.append(res)



print_staks()

for move in moves:
    #move 1
    for i in range(move[0],0,-1):
        letter = staks[move[1]][-1*i]
        staks[move[1]].pop(-1*i)
        staks[move[2]].append(letter)

print('FINAL')
print_staks()

for j in range(num_of_staks):
    print(f'{staks[j+1][-1]}',end ="")
print()
