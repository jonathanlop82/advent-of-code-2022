def sum_values_sprites(v,sprite):
    for n in range(3):
        sprite[n] = sprite[n] + v
    return sprite

def print_crt(cycle):
    for i in range(6):
        for j in range(40):
            print(cycle[i][j],end='')
        print()



with open('list.text') as l:
    lines = l.readlines()

x = 1
cicles = 0
cicles_point = 1
period_cicles = 40
end_cycle = 0
signal_strength = []

cycle = []

for i in range(6):
    l = []
    for j in range(40):
        l.append('.')
    cycle.append(l)

# print_crt(cycle)

sprite_position = [1,2,3]

for line in lines:
    line = line.replace('\n','')
    # print(line)
    instruction = line.split(' ')[0]
    if instruction == 'noop':
        for i in range(1):
            cicles += 1
            # print_crt(cycle)
            if (cicles - end_cycle) in sprite_position:
                cycle[cicles_point - 1][cicles - 1 - end_cycle] = '#'
            if cicles == period_cicles:
                period_cicles += 40
                cicles_point += 1
                end_cycle += 40

                # s_strength = cicles * x
                # signal_strength.append(s_strength)
                # cicles_point = cicles_point + period_cicles
    else:
        value = int(line.split(' ')[1])
        for i in range(2):
            cicles += 1
            # print_crt(cycle)
            if (cicles - end_cycle) in sprite_position:
                cycle[cicles_point - 1][cicles - 1 - end_cycle] = '#'
            if cicles == period_cicles:
                period_cicles += 40
                cicles_point += 1
                end_cycle += 40

                # s_strength = cicles * x
                # signal_strength.append(s_strength)
                # cicles_point = cicles_point + period_cicles
        x += value
        sprite_position = sum_values_sprites(value,sprite_position)
        # print(sprite_position)
        # print_crt(cycle)
        # input()

# print(signal_strength)
# total = 0
# for num in signal_strength:
#     total += num

# print(total)

print_crt(cycle)