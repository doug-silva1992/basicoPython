def count(number):
    total = 0
    for x in number:
        if x < 20:
            total += 1
    return total

list_1 = [1, 3, 7, 15, 23, 43, 56, 98, 17]
print count(list_1)