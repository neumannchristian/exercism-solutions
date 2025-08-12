def commands(binary_str):
    LEGEND = ["wink", "double blink", "close your eyes", "jump"]
    result = []
    binary_str = list(reversed(str(binary_str)))
    result = [LEGEND[switch] for switch, state in enumerate(binary_str[:-1]) if state == "1"]
    return list(reversed(result)) if binary_str[-1] == "1" else result
