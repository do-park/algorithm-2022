A = [0, 1, 1, 1]
def shift_robots(belts):
    temp = [0] + belts[0:2] + [0]
    return temp

print(shift_robots(A))