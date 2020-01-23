from field import Field
import sys


def text_to_map(input_file):
    with open(str(input_file), "r") as inf:
        row = 0
        bomb_coords = set()
        columns_counted = False
        expected_columns = 0
        for line in inf.readlines():
            if line.strip():
                column = 0
                for char in line:
                    if char == ' ' or char == '\t' or char == '\r' or char == '\n':
                        pass
                    elif char == '.':
                        column += 1
                    elif char == 'b' or char == 'B':
                        column += 1
                        bomb_coords.add((column-1, row))
                    else:
                        sys.exit(f'Incorrect data! Invalid symbol "{char}" found!')
                    if expected_columns < column and columns_counted:
                        sys.exit(f'Incorrect data! The row no. {row} was too long!')
                if columns_counted is False:
                    expected_columns = column
                    columns_counted = True
                row += 1
        field_to_return = Field(row, expected_columns, None, 'R')
        if row < 8 or expected_columns < 8:
            sys.exit(f'Incorrect data! The map must not be smaller than 8x8!')
        for coords in bomb_coords:
            field_to_return.place_bombs(coords)
        return field_to_return


def map_to_text(field, output_file):
    with open(str(output_file), 'w') as ouf:
        for y in range(field.y_limit):
            for x in range(field.x_limit):
                val = field.two_dim_field[x][y].get_value()
                if val != 9:
                    ouf.write('.')
                else:
                    ouf.write('B')
            ouf.write('\n')


field = text_to_map('test.txt')
field.show()
map_to_text(field, 'test_output.txt')
