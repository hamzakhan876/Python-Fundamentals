class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        self.borrowed = False

    def book_borrowed(self):
        if self.borrowed:
            print(f'"{self.title}"is already borrowed')
        else:
            self.borrowed = True
            print(f'you borrowed"(self.tit;e)".')
            book1.borrow_book()
            book2.borrowed_book()
    
book1 = Book ("Python Fundamentals","Jazzy",1000)
book2 = Book ("AI for begineers","hamza",5000)
book3 = Book ("Rag Basics","sarim",2000)
book4 = Book ("LLMs Advanced","Akib",3000)

books = [book1,book2,book3,book4]
for book in books:
    print(book.title)
    print(book.author)
    print(book.price)
    print(book.borrowed)