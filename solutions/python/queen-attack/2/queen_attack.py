class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        if row > 7:
            raise ValueError("row not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.column == another_queen.column and self.row == another_queen.row:
            raise ValueError("Invalid queen position: both queens in the same square")
        row_distance = self.row - another_queen.row
        column_distance = self.column - another_queen.column

        return (
            abs(row_distance) == abs(column_distance)
            or row_distance == 0
            or column_distance == 0
        )
