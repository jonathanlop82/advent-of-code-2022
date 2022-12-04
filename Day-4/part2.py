with open('list.text') as l:
    lines = l.readlines()
sum = 0
sum2 = 0

for line in lines:
    line = line.replace('\n','')
    l1 = line.split(',')
    l2 = []
    for k in l1:
        k1 = k.split('-')
        l2 += k1
    e11 = int(l2[0])
    e12 = int(l2[1])
    e21 = int(l2[2])
    e22 = int(l2[3])

    print(l2)
    # Method #2 | Compare first and final digits

    if (e11 >= e21) and (e11 <= e22):
        sum += 1
    elif (e21 >= e11) and (e21 <= e12):
        sum += 1

    print(sum)
print(sum)