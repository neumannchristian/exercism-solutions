def sum_of_multiples(limit, multiples):
    return sum(
        {
            value
            for multiple in multiples
            if multiple != 0
            for value in range(multiple, limit, multiple)
        }
    )
