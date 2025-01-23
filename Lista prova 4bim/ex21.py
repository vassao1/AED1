#def retira(string: str, letra: str) -> str:
#    return "".join([c for c in string.lower() if c != letra])

#print(retira("Antonia Piedade","a"))

def retira(string: str, letra: str) -> str:
    retirada = ''
    codigoletra = ord(letra)
    for i in range(len(string)):
        if string[i] != chr(codigoletra) and string[i] != chr(codigoletra-32):
            retirada += string[i]
    return retirada

print(retira("Antonia Piedade","a"))