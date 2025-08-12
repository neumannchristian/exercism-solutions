def transpose(text):
    if not text:
        return ""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    result = ["" for _ in range(max_len)]
    counter = len(lines)

    for line in lines:
        counter -= 1
        for column_index in range(max_len):
            if len(line) <= column_index:
                if counter != 0:
                    result[column_index] += " "
                continue
            result[column_index] += line[column_index]
    for column_index in range(max_len - 1, -1, -1):
        if result[column_index][len(result[column_index]) - 1] != " ":
            break
        result[column_index] = result[column_index].strip()
    return "\n".join(result)
