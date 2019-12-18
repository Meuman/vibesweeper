from field import Field
from coords import get_neighbor_coords


class Bomb_Field(Field):
    def place_bombs(self, *coordinates):
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
