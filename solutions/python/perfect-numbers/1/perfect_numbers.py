def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors = [1]
    for _ in range(2,number):
        if number % _ == 0: 
            factors.append(_)
    
    if len(factors) == 1 or sum(factors) < number:
        return 'deficient'
    if sum(factors) == number:
        return 'perfect'
    return 'abundant'