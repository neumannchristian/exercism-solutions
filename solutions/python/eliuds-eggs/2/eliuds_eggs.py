def egg_count(display_value):
    count = 0
    quotient = display_value
    while quotient:
        count += quotient % 2
        quotient = quotient // 2
    return count
