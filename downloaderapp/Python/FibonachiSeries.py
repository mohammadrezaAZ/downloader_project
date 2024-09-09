# IsEven Function
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
#Fibonachi series
first = 1
second = 2
sum = 0
while (first < 100):
    if isEven(first) :
        sum = sum + first
    new = first + second
    first = second
    second = new
print ("Sum of even number is : ",sum)  
