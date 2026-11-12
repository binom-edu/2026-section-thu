n = 3**72 + 6*3**50 - 7*3**26 + 2*3**15 + 155
ans = set()
while n:
    ans.add(n % 9)
    n //= 9
print(len(ans))