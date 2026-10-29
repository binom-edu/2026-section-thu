def to3(x):
    ans = ''
    while x:
        ans = str(x % 3) + ans
        x //= 3
    return ans

def r(n):
    t3 = to3(n)
    if n % 3 == 0:
        t3 += t3[-2:]
    else:
        t3 += to3((n % 3) * 5)
    return int(t3, 3)

ans = 10**9
for n in range(1, 10**6):
    if r(n) > 133 and r(n) < ans:
        ans = r(n)
print(ans)