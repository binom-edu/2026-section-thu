def prime_divs(n):
    '''Разложить число на простые множители'''
    ans = []
    d = 2
    while d**2 <= n:
        while n % d == 0:
            ans.append(d)
            n //= d
        d += 1
    if n > 1: ans.append(n)
    return ans

print(prime_divs(100))
print(prime_divs(12))
print(prime_divs(10**9 + 7))
