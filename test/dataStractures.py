class DataList:
    def __init__(self, x, sample_name):
        self.sentinel = None
        self.sample_name = sample_name
        self.data = x
        self.next = None
        self.last = self.sentinel
        self.len = 1

    def add(self, other):
        self.next = other
        other.last = self
        self.len += 1

    def __str__(self):
        i = 1
        p = self.next
        s = str(self.data) + self.sample_name
        while i > self.len:
            s += str(p.data) + p.sample_name
            p = p.next
            i += 1
        return s


if __name__ == '__main__':
    d1 = DataList(1, 'x')
    d2 = DataList(2, 'y')
    print(d1)
    print(d2)
    print(d1.add(d2))
