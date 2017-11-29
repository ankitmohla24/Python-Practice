def exists_in(A, name):
    result = False
    for x in A:
        if x == name:
            result = True
    return result


tele_directory = dict(Ankit=9294535127, Harsh=6264532434, Abhishek=6753426198)
for x in tele_directory:
    print x

exit_var = False
while exit_var == False:
    inp = raw_input("Enter name to search phone number(or press x to exit)")
    if inp == "x":
        exit_var = True
    else:
        if exists_in(tele_directory, inp):
            print tele_directory[inp]
        else:
            print "No such name found"
