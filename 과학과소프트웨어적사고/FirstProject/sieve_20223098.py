import math

n = int(input("n: "))
sieve = [True for i in range(n+1)]
j = 2

for i in range(2, int(math.sqrt(n)+1)):
    if sieve[i] == True:
        while i * j <= n:
            sieve[i * j] = False
            j += 1

for i in range(2, n+1):
    if sieve[i]:
        print(i, end=" ")