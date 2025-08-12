def abbreviate(words):
    stack = []
    acronym = ""
    for idx, char in enumerate(words):
        if char.isalpha():
            stack.append(char)
        if char == " " or char == "-" or idx == len(words) - 1:
            if stack:
                acronym += stack[0].upper()
            stack = []
    return acronym
