high_value = 0
temp_value = 0

with open('list.txt') as l:
    lines = l.readlines()

for line in lines:
    if line == '\n':
        temp_value = 0
    else:
        one_value = int((line).replace('\n',''))
        temp_value += one_value
    
    if temp_value > high_value:
        high_value = temp_value

print(high_value)

    
