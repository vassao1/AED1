npalavras = int(input())
def checkAnagrama(npalavras):
    palavras = [[] for i in range(npalavras)]

    for i in range(npalavras):
        palavras[i].append(input(f"Palavra {i+1}: "))

    for i in palavras:
        lenfirst = len(palavras[0])
        if len(palavras[i]) != lenfirst:
            return False
    
    print(palavras)

print(checkAnagrama(npalavras))