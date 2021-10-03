# 针对图书馆的一个简单的软件系统，会将图书馆建模为图书和读者的一个集合。读书者在任何给定的时间内，最多只能接三本书。
# 每本图书有一个等待借阅的读者列表。每本图书有一个标题、一个作者、已经借阅了它的一名读者，已经等待这本图书还回去后再继续借阅的列表。
# 编写Book和Patron类来建模这些对象。首先考虑每个类的接口或方法，然后为对象的状态选择合适的数据结构。
# 此外，还要编写一个简短的脚本来测试这些类。

class Book:
    def __init__(self, title, author='lisi', reader_borrow=None, reader_wait_list=[]):
        self.title = title
        self.author = author
        self.reader = reader_borrow
        self.wait_list = reader_wait_list

    def __str__(self):
        return 'title:{}\tauthor:{}\treader:{}\twait_list:{}'.format(self.title, self.author, self.reader.name,
                                                                     self.wait_list)

    # def borrow(self, reader):
    #     if self.reader.borrowed < 3:
    #         if self.reader is None:
    #             self.reader = reader
    #         else:
    #             self.wait_list.append(reader)
    #     else:
    #         print('you had lend three book!')
    #
    # def return_book(self):
    #     self.reader = None


class Patron:
    def __init__(self, name):
        self.amount = 3
        self.books = []
        self.borrowed = len(self.books)
        self.name = name

    def __str__(self):
        return 'name:{},borrowed:{},books:{}'.format(self.name, self.borrowed, self.books)

    # def return_book(self, book):
    #     if book in self.books:
    #         self.books.remove(book)
    #         book.return_book()
    #         self.borrowed = self.borrowed - 1
    #     else:
    #         print('logic error!')
    #
    # def borrow_book(self, book):
    #     if self.borrowed < self.amount and book.reader is None:
    #         book.reader = self
    #         self.books.append(book)
    #         self.borrowed = self.borrowed + 1
    #     elif book.reader is not None:
    #         book.wait_list.append(self)


if __name__ == '__main__':
    book1 = Book('nihao')
    book2 = Book('wohao')
    book3 = Book('dajiahao')
    book4 = Book('woshinidie', 'zs')
    p1 = Patron()
    p2 = Patron()
