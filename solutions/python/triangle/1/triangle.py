def isTriangle(sides):
    if len(sides) != 3:
        return False
    if any(x <= 0 for x in sides):
        return False
    a, b, c = sorted(sides)
    return a + b > c

def equilateral(sides):
    return isTriangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return isTriangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return isTriangle(sides) and len(set(sides)) == 3