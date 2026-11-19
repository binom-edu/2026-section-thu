# маска 3?12?14*5
import fnmatch
pat = '3?12?14*5'

def is_valid(n):
    s = str(n)
    return s[0] == '3' and s[2:4] == '12' and s[6:8] == '14' and s[-1] == '5'

for n in range(0, 10**10, 1917):
    # if is_valid(n):
    if fnmatch.fnmatch(str(n), pat):
        print(n, n // 1917)