matrixa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixb = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixc = [[], [], []]

for i in range(3):
    for j in range(3):
        matrixc[i].append(matrixa[i][j] + matrixb[i][j])

for sublist in matrixc:
    for i in sublist:
        print(i, end=" ")
    print()