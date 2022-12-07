def convert(string):
    list1 = []
    list1[:0] = string
    return list1

with open('list.text') as l:
    lines = l.readlines()

datastream = lines[0]

length = len(datastream)
marker = False
count = 0

for i in range(length):
    f = datastream[i:i+14]
    l = convert(f)
    count = 0
    for c in range(14):
        count += l.count(l[c])

    if count == 14:
        print(f'Marker = {i+14}')
        break