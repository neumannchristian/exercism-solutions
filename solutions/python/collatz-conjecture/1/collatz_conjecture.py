def steps(number):
    """Calculate the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.

    Args:
        number (int): The number from which the calculation is performed.

    """

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    steps = 0
    current = number

    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
        steps += 1

    return steps


print(steps(10))
