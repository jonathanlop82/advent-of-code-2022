import re

class Part:

    def __init__(self):   
        self.position = [[1,1]]
        self.count = 1

parts = []
for _ in range(10):
    parts.append(Part())

# print(parts[9].position)

def get_last_position(list):
    # print(list)
    return [(list[-1][0]),(list[-1][1])]

def compare_lists(list1,list2):
    for element in list2:
        # print(f'{element} vs {list1}')
        if (element[0] == list1[0]) and (element[1] == list1[1]):
            # print('Existe')
            return True
    return False

def check_is_far(pos_h,pos_t):
    if ( (pos_h[0] - pos_t[0]) > 1):
        return True, 'R'
    elif ( (pos_h[0] - pos_t[0]) < -1):
        return True, 'L'
    elif ( (pos_h[1] - pos_t[1]) > 1):
        return True, 'U'
    elif ( (pos_h[1] - pos_t[1]) < -1):
        return True, 'D'
    else:
        return False, ''


# def check_last_direction_move(list):
#     new_move = list[-1]
#     last_move = list[-2]
#     if last_move 

def move_next(last_move,new_move,current):
    lx = last_move[0]
    ly = last_move[1]
    nx = new_move[0]
    ny = new_move[1]
    cx = current[0]
    cy = current[1]

    x = nx - lx
    y = ny - ly

    if x == 0 or y == 0:
        return last_move

    elif nx == cx: 
        return [(cx),(cy + y)]
    elif ny == cy:
        return [(cx + x),(cy)]
    else:
        return [(cx + x),(cy + y)]


def print_matriz():
    for y in range(20,-20,-1):
        for x in range(-20,20):
            printed = False
            for k in range(10):
                if (parts[k].position[-1][0] == x) and (parts[k].position[-1][1] == y):
                    print(k,end='')
                    printed = True
            if not(printed):
                if (x == 1) and (y == 1):
                    print('s',end='')
                else:
                    print('.',end='')
            
        print()

with open('list.text') as l:
    lines = l.readlines()

number_regex = re.compile('\d{1,2}')

# print(parts)

for line in lines:
    # print(line)
    direction = line[0]
    steps = number_regex.findall(line)[0]
    steps = int(steps)
    # print(steps)

    if direction == 'R':
        for i in range(steps):
            for p in range(9):
                # for h in range(10):
                #     print(parts[h].position)
                if p == 0:
                    last = get_last_position(parts[p].position)
                    step = last[0] + 1
                    new_pos = [(step),(last[1])]
                    parts[p].position.append(new_pos)
                is_far, new_dir = check_is_far(parts[p].position[-1],parts[p+1].position[-1])
                if is_far:
                    # new_t_pos = [(parts[p].position[-1][0]),(parts[p].position[-1][1])]
                    new_t_pos = move_next(parts[p].position[-2],parts[p].position[-1],parts[p+1].position[-1])
                    if p == 8:
                        if not(compare_lists(new_t_pos,parts[p+1].position)):
                            parts[p+1].count += 1
                    parts[p+1].position.append(new_t_pos)
    elif direction == 'L':
        for i in range(steps):
            for p in range(9):
                # for h in range(10):
                #     print(parts[h].position)
                # print_matriz()
                # input()
                if p == 0:
                    last = get_last_position(parts[p].position)
                    step = last[0] - 1
                    new_pos = [(step),(last[1])]
                    parts[p].position.append(new_pos)
                is_far, new_dir = check_is_far(parts[p].position[-1],parts[p+1].position[-1])
                if is_far:
                    # new_t_pos = parts[p].position[-2]
                    new_t_pos = move_next(parts[p].position[-2],parts[p].position[-1],parts[p+1].position[-1])
                    if p == 8:
                        if not(compare_lists(new_t_pos,parts[p+1].position)):
                            parts[p+1].count += 1
                    parts[p+1].position.append(new_t_pos)
    elif direction == 'U':
        for i in range(steps):
            for p in range(9):
                # for h in range(10):
                #     print(parts[h].position)
                # input()
                if p == 0:
                    last = get_last_position(parts[p].position)
                    step = last[1] + 1
                    new_pos = [(last[0]),(step)]
                    parts[p].position.append(new_pos)
                is_far, new_dir = check_is_far(parts[p].position[-1],parts[p+1].position[-1])
                if is_far:
                    # new_t_pos = parts[p].position[-2]
                    new_t_pos = move_next(parts[p].position[-2],parts[p].position[-1],parts[p+1].position[-1])
                    if p == 8:
                        if not(compare_lists(new_t_pos,parts[p+1].position)):
                            parts[p+1].count += 1
                    parts[p+1].position.append(new_t_pos)
                    
    elif direction == 'D':
        for i in range(steps):
            for p in range(9):
                if p == 0:
                    last = get_last_position(parts[p].position)
                    step = last[1] - 1
                    new_pos = [(last[0]),(step)]
                    parts[p].position.append(new_pos)
                is_far, new_dir = check_is_far(parts[p].position[-1],parts[p+1].position[-1])
                if is_far:
                    # new_t_pos = parts[p].position[-2]
                    new_t_pos = move_next(parts[p].position[-2],parts[p].position[-1],parts[p+1].position[-1])
                    if p == 8:
                        if not(compare_lists(new_t_pos,parts[p+1].position)):
                            parts[p+1].count += 1
                    parts[p+1].position.append(new_t_pos)

    # print_matriz()
    # input()
                    
# print(h_position)
# print()
# for h in range(10):
#     print(parts[h].position) 
# print()
# print_matriz()
# print(parts[9].position)
print(parts[9].count)

