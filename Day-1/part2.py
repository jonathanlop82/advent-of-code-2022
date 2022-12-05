high_value = 0
temp_value = 0
list_numbers = []
final_sum = 0

with open('list.txt') as l:
    lines = l.readlines()

for line in lines:
    if line == '\n':
        list_numbers.append(temp_value)
        temp_value = 0
    else:
        one_value = int((line).replace('\n',''))
        temp_value += one_value
    
    if temp_value > high_value:
        high_value = temp_value

list_numbers.sort()
for num in list_numbers[:-4:-1]:
    final_sum += num

print(final_sum)