import numpy


class Field:
    """
    This is the field module
    It represents the field which is filled with mines, which the player has to avoid setting off.
    A bomb is represented by B.
    An empty space is represented by a 0 value.
    Any other numerical value represents how many bombs are in the neighboring squares.
    """
    def __init__(self, columns, rows):
        """
        The constructor method takes 2 integers as its arguments, columns and rows.
        It makes a two dimensional list with using the arguments to determine the size of the dimensions.
        It fills the list with the number 0, which represent an empty space.
        """
        self.two_dim_field = numpy.full((columns, rows), '0')

    def __str__(self):
        return str(self.two_dim_field)

    def fill_with_bombs(self, *coordinates):
        """
        This method takes the arguments (which are tuples) that represent coordinates (x, y)
        and fills these places with bombs (B)

        """
        for coordinate in coordinates:
            y = coordinate[0]-1  # arrays and lists start from 0 so subtract one
            x = coordinate[1]-1  # same here
            self.two_dim_field[x][y] = 'B'
            # now we have to change the values of the neighboring squares if they are an int,



field = Field(5, 5)
field.fill_with_bombs((2, 5), (2, 4), (3, 2), (1, 1))
print(field)
