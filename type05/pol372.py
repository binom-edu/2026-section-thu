def r(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    return int(b, 2)

for n in range(10000):
    if r(n) > 50:
        print(n)
        break