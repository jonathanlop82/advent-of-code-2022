with open('list.text') as l:
    lines = l.readlines()

x = 1
cicles = 0
cicles_point = 20
period_cicles = 40
signal_strength = []

for line in lines:
    line = line.replace('\n','')
    # print(line)
    instruction = line.split(' ')[0]
    if instruction == 'noop':
        for i in range(1):
            cicles += 1
            if cicles == cicles_point:
                s_strength = cicles * x
                signal_strength.append(s_strength)
                cicles_point = cicles_point + period_cicles
    else:
        value = int(line.split(' ')[1])
        for i in range(2):
            cicles += 1
            if cicles == cicles_point:
                s_strength = cicles * x
                signal_strength.append(s_strength)
                cicles_point = cicles_point + period_cicles
        x += value

print(signal_strength)
total = 0
for num in signal_strength:
    total += num

print(total)