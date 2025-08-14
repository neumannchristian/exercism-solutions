def egg_count(display_value):
    count = 0
    quotient = display_value
    remainder = None
    while quotient > 0:
        remainder = quotient % 2
        count += remainder
        quotient = quotient // 2
    return count
