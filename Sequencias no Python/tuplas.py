x = (40, 41, 42)
print(x)

y = 50, 51, 52
print(y)

a, b, c = 1, 4, 6
print(c)

print(x[0])

list = [x, y]
print(list)

(age, years_of_school) = "30, 17".split(',')
print(age)
print(years_of_school)

def square_info(x):
    A = x ** 2
    P = 4 * x
    print ("Area and Perimeter:")
    return A,P

print(square_info(3))
