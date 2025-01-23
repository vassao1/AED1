lista = [i for i in range(0,16)]
diferentes = [[lista[i] for i in range(1,10)], [lista[i] for i in range(8,14)], [i for i in lista if i % 2 == 0],  [i for i in lista if i % 2 != 0], [i for i in lista[::-1]]]


for sublist in diferentes:
    for j in sublist:
        print(j, end=" ")
    print()