def is_prime(n):
    '''Является ли число n простым'''
    if n == 1: return False
    d = 2
    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print(is_prime(4))
print(is_prime(5))
print(is_prime(10**9 + 7))
print(is_prime(1))