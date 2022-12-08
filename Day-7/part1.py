
with open('list.text') as l:
    lines = l.readlines()

sub = False
current_directory = '/'
tree_directory = []
deep = 0
dirs = {}
sumtotal = 0

for line in lines:
    line = line.replace('\n','')
    if '$ cd ..' == line:
        deep -= 1
        # print(f'Back to directory: {tree_directory[deep - 1]}')
        tree_directory.pop(-1)
        sub = False
        # print(tree_directory)
    elif '$ cd' in line:
        tree = ''.join(tree_directory)
        current_directory = tree + line.split(' ')[2]
        tree_directory.append(current_directory)
        deep += 1
        sub = False
        # print(tree_directory)
    elif '$ ls' == line:
        # print(f'Directory {current_directory}')
        dirs[current_directory] = 0
        sub = True
        continue

    
    if sub:
        element = line.split(' ')
        if element[0] == 'dir':
            # print(element[1])
            pass
        else:
            size = int(element[0])
            sumtotal += size
            # print(current_directory)
            # print(f'Suma {size} a_: {current_directory}')
            dirs[current_directory] += size
            for i in range(1,len(tree_directory)):
                # print(f'Suma {size} a: {tree_directory[i - 1]}')
                dirs[tree_directory[i - 1]] += size
            # if current_directory != '/':
            #     print(f'Suma {size} a: {tree_directory[deep - 2]}')
            #     dirs[tree_directory[deep - 2]] += size

print(dirs)
print(sumtotal)
total = 0
for k in dirs:
    if dirs[k] <= 100000:
        # print(f'{k} = {dirs[k]}')
        total += dirs[k]

print(total)