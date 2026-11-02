class Book: #define book class
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

class BookList:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def __str__(self):
        return f'BookList with {len(self.books)} books: {", ".join(str(book) for book in self.books)}'

book1 = Book('Introduction to Algorithms (3rd ed.)', ['Cormen', 'Leiserson', 'Rivest', 'Stein'], 2009)
book2 = Book('Clean Code', ['Martin'], 2008)
book3 = Book('The Pragmatic Programmer', ['Hunt', 'Thomas'], 1999)

books = [book1, book2, book3]

# sort by number of authors, descending
books.sort(key=lambda b: b.num_authors(), reverse=True)

for book in books:
    print(book)
book_list = BookList()
book_list.add_book(book1)
book_list.add_book(book2)
book_list.add_book(book3)
print(book_list)