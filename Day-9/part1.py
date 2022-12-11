import re

def get_last_position(list):
    # print(list)
    return [(list[-1][0]),(list[-1][1])]

def compare_lists(list1,list2):
    for element in list2:
        if (element[0] == list1[0]) and (element[1] == list1[1]):
            return True
    return False

def check_is_far(pos_h,pos_t):
    if ( abs(pos_h[0] - pos_t[0]) > 1) or ( abs(pos_h[1] - pos_t[1]) > 1):
        return True
    else:
        return False


with open('list.text') as l:
    lines = l.readlines()

number_regex = re.compile('\d{1,2}')

routes = []

t_count = 1

h_position = [[1,1]]
t_position = [[1,1]]


for line in lines:
    direction = line[0]
    steps = number_regex.findall(line)[0]
    steps = int(steps)
    if direction == 'R':
        for i in range(steps):
            last = get_last_position(h_position)
            step = last[0] + 1
            new_pos = [(step),(last[1])]
            h_position.append(new_pos)
            if check_is_far(new_pos,t_position[-1]):
                new_t_pos = h_position[-2]
                if not(compare_lists(new_t_pos,t_position)):
                    t_count += 1
                t_position.append(new_t_pos)
    elif direction == 'L':
        for i in range(steps):
            last = get_last_position(h_position)
            step = last[0] - 1
            new_pos = [(step),(last[1])]
            h_position.append(new_pos)
            if check_is_far(new_pos,t_position[-1]):
                new_t_pos = h_position[-2]
                if not(compare_lists(new_t_pos,t_position)):
                    t_count += 1
                t_position.append(new_t_pos)
    elif direction == 'U':
        for i in range(steps):
            last = get_last_position(h_position)
            step = last[1] + 1
            new_pos = [(last[0]),(step)]
            h_position.append(new_pos)
            if check_is_far(new_pos,t_position[-1]):
                new_t_pos = h_position[-2]
                if not(compare_lists(new_t_pos,t_position)):
                    t_count += 1
                t_position.append(new_t_pos)
    elif direction == 'D':
        for i in range(steps):
            last = get_last_position(h_position)
            step = last[1] - 1
            new_pos = [(last[0]),(step)]
            h_position.append(new_pos)
            if check_is_far(new_pos,t_position[-1]):
                new_t_pos = h_position[-2]
                if not(compare_lists(new_t_pos,t_position)):
                    t_count += 1
                t_position.append(new_t_pos)

# print(h_position)
# print()
# print(t_position)
# print()
print(t_count)
