def isPrime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime

for i in range(1, 10):
    print (i , isPrime(i))
