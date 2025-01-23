x = int(input())
xorig = x
y = int(input())
i = 1

while i < y:
    x *= xorig
    i += 1

print(x)