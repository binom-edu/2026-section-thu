a = [True, False, True]
print(all(a))
print(any(a))

a = [2, 3, 6, 10]
print(all(i % 2 == 0 for i in a))