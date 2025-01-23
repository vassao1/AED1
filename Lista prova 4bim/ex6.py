def main():
    lista1 = []
    lista2 = []
    lista3 = []
    
    print("Informe 5 números em ordem crescente para a lista:")
    for _ in range(5):
        lista1.append(int(input()))
    
    print("Informe 5 números em ordem crescente para a lista:")
    for _ in range(5):
        lista2.append(int(input()))

    lista3 = sorted(lista1 + lista2)

    print("Lista 3:", lista3)
    print("Soma dos elementos de Lista 3:", sum(lista3))
    
main()