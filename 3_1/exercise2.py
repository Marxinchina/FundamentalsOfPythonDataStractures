import exercise1 as e1

for i in [1000, 2000, 4000, 10000, 100000]:
    p = e1.Count(i)
    p.use()
    print('{}:{}'.format(i, p.count))
