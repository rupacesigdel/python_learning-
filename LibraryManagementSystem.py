class library():
    def __init__(self):
        self.numBooks = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.numBooks = len(self.books)

    
    def showInfo(self):
        print(f"The libary has {self.numBooks} books.The books are  ")
        for book in self.books:
            print(book)


MyLibrary = library()
MyLibrary.add_book("science")
MyLibrary.add_book("math")
MyLibrary.add_book("English")
MyLibrary.add_book("Nepali")
MyLibrary.add_book("Social")
MyLibrary.showInfo()
