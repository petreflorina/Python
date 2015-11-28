from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Book(object):
    def __init__(self, title, author, publisher, language, isbn, quantity, pages, price, publication_date, category):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.language = language
        self.isbn = isbn
        self.quantity = quantity
        self.pages = pages
        self.price = price
        self.publication_date = publication_date
        self.category = category


class BookStore(object):
    books = []
    count = 0

    def __init__(self, url):

        """

        :rtype: object
        """
        self.url = url
        self.page = requests.get(url)
        self.data = self.page.text
        self.soup = BeautifulSoup(self.data)

        for title in self.soup.findAll('title'):
            self.books.append(Book('','','','',0,0,0,0,0,''))
            self.count += 1

    def test(self, st):
    	index = 0
    	for x in self.soup.findAll(st):
    		self.books[index].st = st.string
    		index += 1

    def book_init(self):

        test('title')
        
        index = 0
        for author in self.soup.findAll('author'):
            self.books[index].author = author.string
            index += 1
        index = 0
        for publisher in self.soup.findAll('publisher'):
            self.books[index].publisher = publisher.string
            index += 1
        index = 0
        for language in self.soup.findAll('language'):
            self.books[index].language = language.string
            index += 1
        index = 0
        for isbn in self.soup.findAll('isbn'):
            self.books[index].isbn = isbn.string
            index += 1

        index = 0
        for quantity in self.soup.findAll('quantity'):
            self.books[index].quantity = quantity.string
            index += 1

        index = 0
        for pages in self.soup.findAll('pages'):
            self.books[index].pages = pages.string
            index += 1

        index = 0
        for price in self.soup.findAll('price'):
            self.books[index].price = price.string
            index += 1

        index = 0
        for publication_date in self.soup.findAll('publication_date'):
            self.books[index].publication_date = publication_date.string
            index += 1

        index = 0
        for category in self.soup.findAll('category'):
            self.books[index].category = category.string
            index += 1


    def book_print(self):
        for index in range(self.count):
            print self.books[index].title, ' ', self.books[index].author, ' ', self.books[index].publisher, ' ', self.books[index].publication_date

url = 'https://today.java.net/images/2007/04/books.xml'
b = BookStore(url)
b.book_init()
b.book_print()
