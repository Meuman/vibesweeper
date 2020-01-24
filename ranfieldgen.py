from field import Field
from random import randint
from coords import get_neighbor_coords


def generate_random_field(rows, columns, bombs, nobomb_x=-5, nobomb_y=-5):
    if rows*columns - bombs < 9:
        raise Exception('Too many bombs!')
        return
    field = Field(rows, columns, None, 'H')
    while bombs != 0:
        not_here = False
        x = randint(0, columns-1)
        y = randint(0, rows - 1)
        random_tile = field.two_dim_field[x][y]
        neighbor_dict = get_neighbor_coords(nobomb_x, nobomb_y)
        if random_tile.get_value() != 9:
            for coords in neighbor_dict:
                if (x, y) == coords or (x, y) == (nobomb_x, nobomb_y):
                    not_here = True
            if not not_here:
                field.place_bombs((x, y))
                bombs -= 1
    return field
