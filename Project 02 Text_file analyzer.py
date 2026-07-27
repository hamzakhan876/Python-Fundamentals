file  = open("Data.Txt", "w")
file.write("Iam learning Python!")
file.close()

file = open("Data.Txt", "r")
data = file.read()
file.close()


file = open("Data.Txt", "a")
file.write("\nIam Enjoying it!")
file.write("\nPython is easy")
file.write("\nI like Python")
file.close()


file = open("Data.Txt","r")

text = file.read()

file.close()

lines = text.split("\n")

print(len(lines))

words = text.split()

unique_words = set(words)

common_words = set(words)

def menu():
    print("========= TEXT FILE ANALYZER =========")
    print("Total Lines :", len(lines))
    print("Total Words :", len(words))
    print("Unique Words:", len(unique_words))
    print("common Words:", len(common_words))

menu()
