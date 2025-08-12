literal_map = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def roman(number):
    result = ""
    remainder = number

    for multiplier in sorted(literal_map.keys(), reverse=True):
        times = remainder // multiplier
        remainder = remainder % multiplier
        result += literal_map[multiplier] * times
    return result
