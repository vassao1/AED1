matrix = [[x for x in range(1, 11)] for j in range(5)]

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()