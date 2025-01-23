n = int(input())
i = 1
divisores = []

while i <= n:
    if n % i == 0:
        divisores.append(i)
    i += 1

print(divisores)