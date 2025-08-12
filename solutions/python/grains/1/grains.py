def square(number):
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    board = {}
    board[1] = 1
    current = 1
    for field in range(2,65):
        current = current * 2
        board.setdefault(field, current)
    return board.get(number)
        


def total():
    board = {}
    board[1] = 1
    current = 1
    for field in range(2,65):
        current = current * 2
        board.setdefault(field, current)
    return sum(board.values())