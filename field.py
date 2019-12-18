def get_neighbor_coords(x, y):
    coords = dict()
    coords['top left'] = (x-1, y-1)
    coords['top'] = (x, y-1)
    coords['top right'] = (x+1, y-1)
    coords['left'] = (x-1, y)
    coords['right'] = (x+1, y)
    coords['bot left'] = (x-1, y+1)
    coords['bot'] = (x, y+1)
    coords['bot right'] = (x+1, y+1)
    return coords


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

    def fill_with_bombs(self, *coordinates):
        for coordinate in coordinates:
            x = coordinate[0]-1  # arrays and lists start from 0 so subtract one
            y = coordinate[1]-1  # same here
            self.two_dim_field[x][y] = 9
            # now we have to change the values of the neighboring squares if they aren't a mine
            neighbor_coords = get_neighbor_coords(x, y)
            for coords in neighbor_coords.values():
                try:
                    this_tile = self.two_dim_field[coords[0]][coords[1]]
                    if this_tile != 9 and (0 <= coords[0] <= self.x_limit-1) and (0 <= coords[1] <= self.y_limit-1):
                        self.two_dim_field[coords[0]][coords[1]] += 1
                except Exception:  # not really sure how the fuck should i handle this exception or should i even handle it at all
                    pass  # this try is really just here because the interpreter shits itself if it sees an index out of range
                # also it's way easier to use try/except instead of writing a shitton of if statements (this comment was made by ask for forgiveness, not permission gang)


field = Field(5, 5)
field.fill_with_bombs((1, 1), (5, 1,), (1, 5), (5, 5))
print(field.show())
