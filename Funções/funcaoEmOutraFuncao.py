def wage(w_hour):
    return w_hour * 25

def with_bonus(w_hour):
    return wage(w_hour) + 50

print(wage(8), with_bonus(8))