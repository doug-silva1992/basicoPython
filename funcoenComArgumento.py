def subtract_bc(a, b, c):
    result = a - b * c
    print('Parameter b equals', a)
    print('Parameter b equals', b)
    print('Parameter b equals', c)
    return result

print(subtract_bc(10, 3, 2))
print('\r')
print(subtract_bc(a = 10, b = 3, c = 2))
