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

# print(trees_on_edge)

count = 0
best_house = 0
for i in range(1,columns - 1):
    for j in range(1,rows - 1):
        tree = mat[i][j]
        #Right
        right = 0
        left = 0
        top = 0
        down = 0
        # print(f'Tree:{tree}')
        for r in range(j - 1,-1,-1):
            # print(f'Is {tree} > {mat[i][r]}')
            if tree > mat[i][r]:
                right = right + 1
            else:
                right = right + 1
                break
        # print(right)
        #Left
        for l in range(j+1,columns):
            if tree > mat[i][l]:
                left = left + 1
            else:
                left = left + 1
                break

        # print(left)
        #top
        for t in range(i - 1,-1,-1):
            if tree > mat[t][j]:
                top = top + 1
            else:
                top = top + 1
                break
        # print(top)
        #Down
        for d in range(i+1,rows):
            if tree > mat[d][j]:
                down = down + 1
            else:
                down = down + 1
                break
        # print(down)
        
        if (right * left * down * top) > best_house:
            best_house = right * left * down * top 
        

print(best_house)


