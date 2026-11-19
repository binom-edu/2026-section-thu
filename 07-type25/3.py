def divs(n):
    '''Найти все делители числа n'''
    ans = set()
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            ans.add(d)
            ans.add(n // d)
        d += 1
    return ans

