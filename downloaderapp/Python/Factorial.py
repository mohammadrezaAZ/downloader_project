n = int(input('Enter your number: '))
fact = 1
for i in range(1,n+1):
    fact *= i
    print('factorial is: ',fact)

# def factorial(n):
#     if (n <= 1):
#         return n
#     else:
#         sub = factorial(n - 1)
#         fact = sub * n
#         return fact