file = open("myname.txt", "w")
file.write("My name is Hamza Ahmed khan")
file.close()


file = open("myname.txt", "r")
data = file.read()
print(data)
file.close()