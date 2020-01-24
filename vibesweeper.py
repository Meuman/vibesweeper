import sys
from game import Game
from parser import *
from ranfieldgen import generate_random_field


def vibesweeper(mode, rows_or_field=None, columns=None, num_of_bombs=None, path=None):
    if mode == 0:
        this_game = Game(int(mode), int(rows_or_field), int(columns), num_of_bombs)
    elif mode == 1:
        field = text_to_map(str(rows_or_field))
        game = Game(1, field)
    elif mode == 2:
        field = generate_random_field(rows_or_field, columns, num_of_bombs)
        map_to_text(field, str(path))


vibesweeper(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]))
# try:
#     vibesweeper(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), None)
# except Exception:
#     pass
