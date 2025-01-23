n = int(input())
numlist = []
negativenums = []
positivenums = []

for _ in range(n):
    numlist.append(int(input()))

for i in numlist:
    if i < 0:
        negativenums.append(i)
    else:
        positivenums.append(i)
        
print(negativenums, positivenums, numlist)