def score(x, y):
    probe = x**2 + y**2
    rules = (1, 10), (25, 5), (100, 1), (200, 0)

    for distance, points in rules:
        if probe <= distance: return points
