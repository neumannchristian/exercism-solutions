def transpose(text):
    result = []
    for row, line in enumerate(text.splitlines()):
        for column, char in enumerate(line):
            while len(result) <= column:
                result.append([])
            while len(result[column]) < row:
                result[column].append(" ")
            result[column].append(char)
    return "\n".join("".join(row) for row in result)
