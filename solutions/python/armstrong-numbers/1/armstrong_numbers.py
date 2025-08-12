def is_armstrong_number(n):
    sep = [*str(n)]
    return True if n == sum(list(map(lambda x: int(x)**len(sep) ,sep))) else False