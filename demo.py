from scipy.special import comb

n = 71
k = 43
sum = 0
for i in range(k, n + 1):
    sum = sum + comb(n, i) * 0.5 ** i * 0.5 ** (n - i)

print(sum)
