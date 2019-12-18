class Field:
    def __init__(self, rows, columns):
        self.x_limit = columns
        self.y_limit = rows
        self.two_dim_field = [[0 for y in range(rows)] for x in range(columns)]

    def show(self):
        for y in range(self.y_limit):
            for x in range(self.x_limit):
                print(self.two_dim_field[x][y], end=' ')
            print()
