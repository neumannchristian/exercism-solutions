import math


def factors(value):
    result = []
    while value % 2 == 0:
        result.append(2)
        value = value / 2

    for i in range(3, int(math.sqrt(value)) + 1, 2):
        while value % i == 0:
            result.append(i)
            value = value / i

    if value > 2:
        result.append(value)
    return result
