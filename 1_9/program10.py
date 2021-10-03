# 编写一个Library类，它能够管理program9里的图书和读者。
# 这个类应该包含添加、删除和查找图书和读者的方法，还应该有借阅和归还图书的方法。
# 编写一段脚本来测试所有这些方法
from program9 import *


class Library:
    def __init__(self, books=None, readers=None):
        if books is None:
            books = []
        if readers is None:
            readers = []
        self.books = books
        self.readers = readers

    def borrow_book(self, reader, book):
        if book in self.books:
            if reader.borrowed < reader.amount:
                if book.reader is None:
                    book.reader = reader
                    reader.books.append(book)
                    reader.borrowed = 1 + reader.borrowed
                    print('{} had lent {}'.format(reader.name, book.title))
                else:
                    book.wait_list.append(reader)
            else:
                print('you had lent three books yet!')
                book.wait_list.append(reader)
        else:
            print('we have no {}'.format(book.title))

    def return_book(self, book):
        if book in self.books:
            if book.reader is None:
                print('{} is belong to nobody'.format(book.title))
            else:
                reader = book.reader
                book.reader = None
                reader.borrowed = reader.borrowed - 1
                reader.books.remove(book)
        else:
            print('the book is not belong to us,but ...')
            self.books.append(book)

    def add_books(self, books):
        for book in books:
            if book in self.books:
                print('logic error!')
            else:
                self.books.append(book)

    def del_books(self, books):
        for book in books:
            if book in self.books:
                self.books.remove(book)
            else:
                print('wo have no {},can\'t do it'.format(book.title))

    def del_readers(self, readers):
        for reader in readers:
            if reader in self.readers:
                self.readers.remove(reader)
            else:
                print('can\'t do it,we have no {}'.format(reader.name))

    def add_readers(self, readers):
        for reader in readers:
            if reader not in self.readers:
                self.readers.append(reader)
            else:
                print('we had {} yet.'.format(reader.name))

    def seek_book(self, title):
        for book in self.books:
            if title == book.title:
                print(book)
        else:
            print('查无此书')

    def seek_reader(self, name):
        for reader in self.readers:
            if reader.name == name:
                print(reader)
        else:
            print('查无此人')


if __name__ == '__main__':
    book1 = Book('book1')
    book2 = Book('book2')
    book3 = Book('book3')
    book4 = Book('book4', 'zs')
    p1 = Patron('p1')
    p2 = Patron('p2')
    library = Library([book1, book2, book3, book4], [p1, p2])
    library.borrow_book(p1, book1)
    library.return_book(book4)
    library.seek_reader('p1')
