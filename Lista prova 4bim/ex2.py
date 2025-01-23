n = int(input())
numlist = []
negativenums = []
positivenums = []
zerocount = 0

for _ in range(n):
    numlist.append(int(input()))

for i in numlist:
    if i < 0:
        negativenums.append(i)
    elif i > 0:
        positivenums.append(i)
    else:
        zerocount += 1
        
print(f"{negativenums}, {positivenums}, {numlist}, Número de zeros: {zerocount}")