class SavingsAccount:
    def __init__(self, name, pin, balance):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __lt__(self, other):
        return self._name < other._name

    # def __gt__(self, other):
    #     return self._name > other._name

    def __eq__(self, other):
        return self._name == other._name


if __name__ == '__main__':
    s1 = SavingsAccount('Lisi', '1000', 0)
    s2 = SavingsAccount('zs', '1001', 30)
    print(s1 > s2)
    print(s1 == s2)
    print(s1 < s2)
    s3 = SavingsAccount('Lisi', '1000', 0)
    print(s1 == s3)
