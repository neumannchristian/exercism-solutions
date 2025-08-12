from string import ascii_uppercase

def rows(letter):
    max_idx = ascii_uppercase.index(letter)
    row_size = (max_idx * 2) + 1

    def make_line(idx):
        char = ascii_uppercase[idx]
        outer_spaces = " " * (max_idx - idx)
        if idx == 0:
            return outer_spaces + char + outer_spaces
        inner_spaces = " " * (row_size - 2 - 2 * (max_idx - idx))
        return outer_spaces + char + inner_spaces + char + outer_spaces

    top = [make_line(idx) for idx in range(max_idx + 1)]
    bottom = [make_line(idx) for idx in range(max_idx - 1, -1, -1)]
    return top + bottom
