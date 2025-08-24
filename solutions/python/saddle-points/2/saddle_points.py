def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    row_maxima = [max(row) for row in matrix]
    col_minima = [min(col) for col in list(zip(*matrix))]

    coordinates = []

    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if value == row_maxima[r] and value == col_minima[c]:
                coordinates.append({"row": r + 1, "column": c + 1})

    return coordinates
