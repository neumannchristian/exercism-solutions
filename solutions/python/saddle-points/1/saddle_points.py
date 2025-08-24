def saddle_points(matrix):
    if not matrix:
        return []

    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("irregular matrix")

    max_in_rows = [max(row) for row in matrix]
    tallest_collection = [
        [j for j, val in enumerate(row) if val == max_in_rows[i]]
        for i, row in enumerate(matrix)
    ]

    min_in_cols = [min(col) for col in zip(*matrix)]
    smallest_collection = [
        [i for i, val in enumerate(col) if val == min_in_cols[j]]
        for j, col in enumerate(zip(*matrix))
    ]

    saddle_points = []

    for i in range(len(matrix)):
        for j in tallest_collection[i]:
            if i in smallest_collection[j]:
                saddle_points.append({"row": i + 1, "column": j + 1})

    return saddle_points
