import math


def factors(value):
    result = []
    while value % 2 == 0:
        result.append(2)
        value /= 2

    for idx in range(3, int(math.sqrt(value)) + 1, 2):
        while value % idx == 0:
            result.append(idx)
            value /= idx

    if value > 2:
        result.append(value)
    return result
