def calculate(num1,num2):
    if num2 == 0:
        return "undefined"
    else:
        return (num1+num2)/num2


num1 = input("Enter a number")
num2 = input("Enter another number")
print (calculate(num1,num2))