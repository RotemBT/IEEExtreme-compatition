
size = int(input('Size of 2d: '))
mat = [list(map(int, input().split())) for i in range(size)]

sumDiagonal = 0
wrongList = []
count = 0
sumDiagonal2 = 0
# checking the main diagonal
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i == j:
            sumDiagonal += mat[i][j]

# checking the second diagonal by reverse the matrix
copiedMatrix = mat.copy()
copiedMatrix = copiedMatrix[::-1]
for i in range(len(copiedMatrix)):
    for j in range(len(copiedMatrix[0])):
        if i == j:
            sumDiagonal2 += copiedMatrix[i][j]
if sumDiagonal != sumDiagonal2:
    wrongList.append(0)
    count += 1
# checking the rows
for i in range(len(mat)):
    sum = 0
    for j in range(len(mat[0])):
        sum += mat[i][j]
    if sum != sumDiagonal:
        wrongList.append(i + 1)
        count += 1
# checking the column by transpose
for j in range(len(mat[0])):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][j]
    if sum != sumDiagonal:
        wrongList.append(-j - 1)
        count += 1

print(count)
for i in sorted(wrongList, reverse=False):
    print(i)
