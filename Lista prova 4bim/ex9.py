tabuleiro = [[1,2,3], [4,5,6], [7,8,9]]

def printTabuleiro():
    for sublist in tabuleiro:
        for j in sublist:
            print(j, end=" ")
        print()
        
def checkVitoria(tabuleiro):
    # Vitória por linha
    for sublist in tabuleiro:
        if sublist[0] == sublist[1] == sublist[2]:
            if sublist[0] == "X":
                print("Jogador 1 venceu!")
                return True
            elif sublist[0] == "O":
                print("Jogador 2 venceu!")
                return True
    # Vitória por coluna
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:
            if tabuleiro[0][i] == "X":
                print("Jogador 1 venceu!")
                return True
            elif tabuleiro[0][i] == "O":
                print("Jogador 2 venceu!")
                return True
    # Vitória por diagonal
    if (tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X") or (tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X"):
        print("Jogador 1 venceu!")
        return True
    if (tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O") or (tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O"):
        print("Jogador 2 venceu!")
        return True

for i in range(10):
    printTabuleiro()
    if i % 2 == 0:
        print("Vez do jogador 1")
        valida = False
        while valida == False:
            j1input = int(input("Digite a posição: "))
            for sublist in tabuleiro:
                if j1input in sublist:
                    sublist[sublist.index(j1input)] = "X"
                    valida = True
    elif i == 9:
        print("Empate")
    else:
        print("Vez do jogador 2")
        valida = False
        while valida == False:
            j2input = int(input("Digite a posição: "))
            for sublist in tabuleiro:
                if j2input in sublist:
                    sublist[sublist.index(j2input)] = "O"
                    valida = True
    if checkVitoria(tabuleiro):
        printTabuleiro()
        break