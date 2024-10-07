class Book:

    def __init__(self, title, year):

        self.author = "Stephen Hawkings"
        self.title = title
        self.year = year
    

def printBookArray(books):

    for book in books:
        print(book.title + " written by " + book.author + " in " + book.year)

books = []

books.append(Book("How Did It All Begin?", "2021"))

books.append(Book("The Theory of Everything", "2010"))

books.append(Book("God Created the Integers", "2006"))

printBookArray(books)