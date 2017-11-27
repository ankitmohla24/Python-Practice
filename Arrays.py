def sumoflist(arr):
    result = 0
    for x in range(0, len(arr)):
        result = result + arr[x]
    return result


number = input("Enter the length of List")
List1 = []
for x in range(0, number):
    element = input("Enter element")
    List1.append(element)
print "sum of List is ", sumoflist(List1)
