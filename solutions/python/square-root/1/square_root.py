def square_root(number):
    x = number / 2 
    while True:
        next_x = (x + number / x) / 2
        if abs(next_x - x) < 1e-10:
            return next_x
        x = next_x
    return x