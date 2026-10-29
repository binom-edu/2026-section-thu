def r(n):
    s1 = s2 = 0
    for i in range(10):
        d = n % 10
        if d % 2 == 0:
            s1 += d
        if i % 2 == 0:
            s2 += d
        n //= 10
    return abs(s1 - s2)

for n in range(10 ** 7):
    if r(n) == 26:
        print(n)
        break