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
    fourth = datastream[i:i+4]
    l = convert(fourth)

    # print(f'{l} - {i+4}')
    count = 0
    for c in range(4):
        count += l.count(l[c])

    if count == 4:
        print(f'Marker = {i+4}')
        break

