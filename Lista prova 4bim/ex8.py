matriz = [[],[],[]]
maior = 0

for sublist in matriz:
    for i in range(5):
        sublist.append(int(input()))

for sublist in matriz:
    for j in sublist:
        print(j, end=" ")
        if j > maior:
            maior = j
    print()

print(maior)