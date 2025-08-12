def score(x, y):
    probe = x**2 + y**2

    if probe <= 1:
        return 10     # inner circle
    if probe <= 25:
        return 5      # middle ring
    if probe <= 100:
        return 1      # outer ring
    return 0      # outside the target
