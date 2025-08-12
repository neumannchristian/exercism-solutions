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
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
]

RESISTANCE = {
    "grey" : "0.05",
    "violet" : "0.1",
    "blue" : "0.25",
    "green" : "0.5",
    "brown" : "1",
    "red" : "2",
    "gold" : "5",
    "silver" : "10",
}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms" 
    first_digit = COLOR_LIST.index(colors[0])
    second_digit = COLOR_LIST.index(colors[1])
    if len(colors) == 5:
        third_digit = COLOR_LIST.index(colors[2])
        zeroes = COLOR_LIST.index(colors[3])
        value = ((first_digit*100)+second_digit*10+third_digit)*10**zeroes
    else:
        zeroes = COLOR_LIST.index(colors[2])
        value = ((first_digit*10)+second_digit)*10**zeroes

    for factor, prefix in UNITS:
        if value >= factor:
            ohms = value / factor
            return f"{int(ohms) if ohms.is_integer() else ohms} {prefix}ohms ±{RESISTANCE.get(colors[-1])}%"

    return f"{value} ohms ±{RESISTANCE.get(colors[-1])}%" 
