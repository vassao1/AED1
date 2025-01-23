def retira(lista: list, letra: str) -> list:
    return [i for i in lista if i != letra]

print(retira(["a","b","c","a","f","a","a","k"],"a"))