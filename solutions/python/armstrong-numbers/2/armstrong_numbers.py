def is_armstrong_number(n):
    n_str = str(n)
    power = len(n_str)
    return n == sum(int(digit) ** power for digit in n_str)