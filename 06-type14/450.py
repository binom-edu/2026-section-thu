def f(x, y):
    a = '7x589y'.replace('x', x).replace('y', y)
    b = 'EExy9AC'.replace('x', x).replace('y', y)
    return int(a, 17) + int(b, 17)


alf = '0123456789ABCDEF'

for x in alf:
    if all(f(x, y) % 13 == 0 for y in alf):
        print(f(x, '3') // 13)
        break