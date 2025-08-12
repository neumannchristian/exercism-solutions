COLOR_LIST = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

UNITS = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
]

def label(colors):
    a ,b ,c = colors[:3]
    first_digit = COLOR_LIST.index(a)
    second_digit = COLOR_LIST.index(b)
    zeroes = COLOR_LIST.index(c)
    value = ((first_digit*10)+second_digit)*10**zeroes

    for factor, unit in UNITS:
        if value >= factor: 
            return f"{value // factor} {unit}"

    return f"{value} ohms" 
