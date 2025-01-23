string = input()
blankcount = 0
maior = 0

for i in range(len(string)):
    while string[i] == " ":
        blankcount += 1
        i += 1
    if maior < blankcount:
        maior = blankcount
    blankcount = 0

print(maior)