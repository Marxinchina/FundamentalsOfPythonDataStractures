# 编写一个程序，它允许用户在文件行中导航。
# 程序提示用户输入一个文件名，并且输入想要放入到列表中的文本行。
# 然后，程序进入循环中，它会输出文件的行数，并且提示用户输入一个行号。
# 实际的行号范围是从1到文件中的行数。如果用户输入0，程序退出。否则，程序输出和该行号相关的行。

class Navigator:
    def __init__(self, file):
        self.file = file
        with open(self.file) as f:
            lines = f.readlines()
            f.close()
        self.lines = lines
        self.row_num = len(lines)

    def print_row(self, row_num):
        print(self.lines[row_num - 1])


if __name__ == '__main__':
    n = Navigator(input('input a file name: '))
    row_num = n.row_num
    n.print_row(int(input('input row number(1-{}): '.format(row_num))))
