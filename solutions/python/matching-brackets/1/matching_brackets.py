def is_paired(input_string):
    BRACKETS = {"}": "{", "]": "[", ")": "("}
    stack = []

    for char in input_string:
        if char in BRACKETS.values():  # if opening add to stack
            stack.append(char)
        elif char in BRACKETS:  # if closing remove from stack
            if not stack or stack[-1] != BRACKETS[char]:  # abort if mismatch
                return False
            stack.pop()

    return not stack
