#def factorial(n):
#    result = 1
#    while n > 0:
#        result = result * n
#        n = n - 1
#    return result


def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result


number = input("enter a number to calculate its factorial ")
print (factorial(number))