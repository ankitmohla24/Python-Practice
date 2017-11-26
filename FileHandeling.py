file_object = open("Textfile.txt","w")
phrase = "This will be written to the file"
file_object.write(phrase)
file_object.close()

file_object2 = open("Textfile.txt","r")
phrase2 = file_object2.read()
file_object2.close()
print phrase2