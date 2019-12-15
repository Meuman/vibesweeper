import numpy


class Field:
    """
    This is the field module
    It represents the field which is filled with mines, which the player has to avoid setting off.
    A bomb is represented by B.
    An empty space is represented by N.
    """
    def __init__(self, columns, rows):
        """
        The constructor method takes 2 integers as its arguments, columns and rows.
        It makes a two dimensional list with using the arguments to determine the size of the dimensions.
        It fills the list with the letter N, which represent an empty space.
        """
        self.two_dim_field = numpy.full((columns, rows), 'N')

    def __ndarray__(self):
        print(self.two_dim_field)

    def fill_with_bombs(self, *coordinates):
        """
        This method takes the arguments (which are tuples) that represent coordinates (x, y)
        and fills these places with bombs (B)
        """
        for coordinate in coordinates:
            y = coordinate[0]-1  # arrays and lists start from 0 so subtract one
            x = coordinate[1]-1  # same here
            self.two_dim_field[x][y] = 'B'


field = Field(5, 5)
# field.__ndarray__()
field.fill_with_bombs((2, 5))
field.__ndarray__()
