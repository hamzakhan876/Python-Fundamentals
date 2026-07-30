class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


book1 = Book("Data Scientist", "Ahmed", 1000)
book2 = Book("AI Engineer", "Hamza", 2000)
book3 = Book("Python Basics", "Ali", 1500)


print("Book 1")
print(book1.title)
print(book1.author)
print(book1.price)

print()

print("Book 2")
print(book2.title)
print(book2.author)
print(book2.price)

print()

print("Book 3")
print(book3.title)
print(book3.author)
print(book3.price)