def r(n):
    s = str(n)
    a, b, c = int(s[0]), int(s[1]), int(s[2])
    x, y = a * b, b * c
    if x > y: x, y = y, x
    return str(x) + str(y)

for n in range(100, 1000):
    if r(n) == '621':
        print(n)