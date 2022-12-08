with open('list.text') as l:
    lines = l.readlines()

rows = len(lines)
mat = []

for line in lines:
    line = line.replace('\n','')
    temp = []
    for num in line:
        temp.append(num)
    mat.append(temp)
    columns = len(line)

trees_on_edge = (rows*2) + (columns*2) - 4

print(trees_on_edge)

count = 0

for i in range(1,columns - 1):
    for j in range(1,rows - 1):
        tree = mat[i][j]
        #Right
        right = True
        left = True
        top = True
        down = True
        # print(f'Tree:{tree}')
        for r in range(j):
            # print(mat[i][r])
            if tree > mat[i][r]:
                right = right and True
            else:
                right = right and False
        # print(right)
        #Left
        for l in range(j+1,columns):
            if tree > mat[i][l]:
                left = left and True
            else:
                left = left and False

        # print(left)
        #top
        for t in range(i):
            if tree > mat[t][j]:
                top = top and True
            else:
                top = top and False
        # print(top)
        #Down
        for d in range(i+1,rows):
            if tree > mat[d][j]:
                down = down and True
            else:
                down = down and False
        # print(down)
        if right or left or top or down:
            count += 1

print(count)
print(f'Total: {trees_on_edge + count}')