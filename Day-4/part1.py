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

    # Methos #1 | compare strings
    line1 = '-'
    line2 = '-'

    for i in range(e11,e12 + 1):
        line1 += str(i) + '-'
    for j in range(e21,e22 + 1):
        line2 += str(j) + '-'
    if line1 in line2:
        sum2 += 1
    elif line2 in line1:
        sum2 += 1

    
    # Method #2 | Compare first and final digits

    if (e11 >= e21) and (e12 <= e22):
        sum += 1
    elif (e21 >= e11) and (e22 <= e12):
        sum += 1
    

    if sum != sum2:
        input()
    

print(sum2)
print(sum)