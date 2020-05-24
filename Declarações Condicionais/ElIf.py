def compare_to_five(y):
    if y > 5:
        return "Greater"
    elif y < 0:
        return "Negative"
    elif y < 5:
        return "Less"
    else: 
        return "Equal"

print(compare_to_five(3))
print(compare_to_five(-3))
print(compare_to_five(5))