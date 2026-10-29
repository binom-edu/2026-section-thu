def r(n):
    b = bin(n)[2:]
    for i in range(2):
        b += str(b.count('1') % 2)
    return int(b, 2)

for n in range(1, 1000):
    if r(n) > 96:
        print(n)
        break