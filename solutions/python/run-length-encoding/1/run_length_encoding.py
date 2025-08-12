def decode(string):
    result = ""
    multiplyer = ""
    for char in string:
        if char.isdigit():
            multiplyer += char
        else:
            if multiplyer:
                result += int(multiplyer) * char
                multiplyer = ""
            else:
                result += char
    return result


def encode(string):
    if string == "":
        return ""

    result = ""
    count = 0
    last = string[0]
    for idx, char in enumerate(string):
        if char == last:
            count += 1
            if idx == len(string) - 1:
                result += f"{count}{last}"
        else:
            result += f"{count if count > 1 else ''}{last}"
            count = 1
            last = char
            if idx == len(string) - 1:
                result += char
    return result
