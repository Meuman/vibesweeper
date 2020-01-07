import field as f
from coords import get_neighbor_coords


class Game:
    def __init__(self, field=f.Field(5, 5)):
        self.field = field
        self.result = None

    def click_tile(self, x, y):
        x -= 1
        y -= 1
        try:
            self.field.two_dim_field[x][y].reveal()
            if self.field.two_dim_field[x][y].get_value() == 9:
                self.result = False
            self.reveal_surrounding_tiles(x, y)
        except Exception:
            pass

    def reveal_surrounding_tiles(self, x, y):
        x -= 1
        y -= 1
        neighbor_coords = get_neighbor_coords(x, y)
        for coords in neighbor_coords.values():
            try:
                processed_tile = self.field.two_dim_field[coords[0]][coords[1]]
                if processed_tile.state == 'H':
                    if processed_tile.get_value() != 9:
                        processed_tile.reveal()
                    if processed_tile.get_value() == 0:
                        self.reveal_surrounding_tiles(coords[0], coords[1])
            except Exception:
                pass


field = f.Field(5, 5)
game = Game(field)
game.field.place_bombs((1, 1), (3, 3))
game.click_tile(2, 2)
game.field.show()
