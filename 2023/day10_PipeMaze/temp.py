def intersection(l, k):
    j = [value for value in l if value in k]
    return j

a = [(0, 2), (2, 2)]
b = [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2)]

if intersection(a, b):
    print('Hi')
