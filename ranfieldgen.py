from field import Field
from random import randint


def generate_random_field(rows, columns, bombs):
    field = Field(rows, columns)
    while bombs != 0:
        x = randint(0, columns-1)
        y = randint(0, rows - 1)
        random_tile = field.two_dim_field[x][y]
        if random_tile.get_value() != 9:
            field.place_bombs((x, y))
            bombs -= 1
    return field


field = generate_random_field(5, 5, 5)
field.show()
