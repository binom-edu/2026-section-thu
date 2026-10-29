def r(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '00'
    return int(b, 2)

ans = 10**12
for n in range(1, 1000):
    if r(n) < ans and r(n) > 95:
        ans = r(n)
print(ans)
