from coords import get_neighbor_coords
from tile import Tile


class Field:
    def __init__(self, rows, columns, two_dim_field=None, default_state='H'):
        self.x_limit = columns
        self.y_limit = rows
        if two_dim_field is None:
            self.two_dim_field = [[Tile(0, default_state, x, y) for y in range(rows)] for x in range(columns)]
        else:
            self.two_dim_field = two_dim_field

    def show(self):
        for y in range(self.y_limit):
            for x in range(self.x_limit):
                print(self.two_dim_field[x][y], end=' ')
            print()

    def place_bombs(self, *coordinates):
        for coordinate in coordinates:
            x = coordinate[0]
            y = coordinate[1]
            self.two_dim_field[x][y].set_value(9)
            neighbor_coords = get_neighbor_coords(x, y)
            for coords in neighbor_coords:
                try:
                    this_tile_value = self.two_dim_field[coords[0]][coords[1]].get_value()
                    if this_tile_value != 9 and (0 <= coords[0] <= self.x_limit-1) and (0 <= coords[1] <= self.y_limit-1):
                        self.two_dim_field[coords[0]][coords[1]] += 1
                except Exception:
                    pass
