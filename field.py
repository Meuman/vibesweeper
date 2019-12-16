class Field:
    def __init__(self, columns, rows):
        self.y_limit = columns
        self.x_limit = rows
        self.two_dim_field = [[0 for x in range(columns)] for y in range(rows)]

    def show(self):
        for x in range(self.y_limit):
            for y in range(self.x_limit):
                print(f'{self.two_dim_field[y][x]} ', end='')
            print()

    def fill_with_bombs(self, *coordinates):
        for coordinate in coordinates:
            x = coordinate[0]-1  # arrays and lists start from 0 so subtract one
            y = coordinate[1]-1  # same here
            self.two_dim_field[x][y] = 9
            # now we have to change the values of the neighboring squares if they aren't a mine
            if (y > 0):  # case                             top
                a = self.two_dim_field[x][y-1]
                if a != 9:
                    self.two_dim_field[x][y-1] += 1
            if (y < self.y_limit - 1):  # case              down
                a = self.two_dim_field[x][y+1]
                if a != 9:
                    self.two_dim_field[x][y+1] += 1
            if (x > 0):  # case                             left
                a = self.two_dim_field[x-1][y]
                if a != 9:
                    self.two_dim_field[x-1][y] += 1
            if (x < self.x_limit - 1):  # case               right
                a = self.two_dim_field[x+1][y]
                if a != 9:
                    self.two_dim_field[x+1][y] += 1
            if (y > 0 and x > 0):  # case                     top left
                a = self.two_dim_field[x-1][y-1]
                if a != 9:
                    self.two_dim_field[x-1][y-1] += 1
            if (y > 0 and x < self.x_limit - 1):  # case     top right
                a = self.two_dim_field[x+1][y-1]
                if a != 9:
                    self.two_dim_field[x+1][y-1] += 1
            if (y < self.y_limit - 1 and x > 0):  # case     bot left
                a = self.two_dim_field[x-1][y+1]
                if a != 9:
                    self.two_dim_field[x-1][y+1] += 1
            if (y < self.y_limit - 1 and x < self.x_limit - 1):
                a = self.two_dim_field[x+1][y+1]
                if a != 9:
                    self.two_dim_field[x+1][y+1] += 1


field = Field(5, 5)
field.fill_with_bombs((2, 4), (3, 4))
print(field.show())
