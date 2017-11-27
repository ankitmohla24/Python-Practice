def whileloop(n):
    x = 0
    while x < n:
        print "use of while",
        print x,
        print "times"
        x = x + 1


def forloop(n):
    for x in range(0, n):
        print "use of for",
        print x,
        print "times"


number = input("enter a number ")
whileloop(number)
forloop(number)