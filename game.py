import field as f
from coords import get_neighbor_coords
import pygame as pg


class Game:
    def __init__(self, field=f.Field(5, 5)):
        pg.init()
        icon = pg.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\ico.png')
        pg.display.set_icon(icon)
        pg.display.set_caption("Vibesweeper")
        self.RECT_SIZE = 75
        self.field = field
        self.result = None
        self.init_screen()
        self.draw_borders()
        self.init_menu()
        pg.display.update()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

    def init_screen(self):
        self.display_width = self.field.x_limit*self.RECT_SIZE
        self.display_height = (self.field.y_limit + 1)*self.RECT_SIZE
        self.DISPLAY = pg.display.set_mode((self.display_width, self.display_height))

    def init_menu(self):
        self.menurect = pg.Rect(0, 0, self.display_width, self.RECT_SIZE)
        pg.draw.rect(self.DISPLAY, (200, 200, 200), self.menurect)

    def draw_borders(self):
        horizontal_range = self.field.y_limit
        vertical_range = self.field.x_limit
        for horizontal_iterator in range(horizontal_range):
            horizontal_rect = pg.Rect(0, (horizontal_iterator+2)*75, self.display_width, 2)
            pg.draw.rect(self.DISPLAY, (255, 0, 0), horizontal_rect)
        for vertical_iterator in range(vertical_range):
            vertical_rect = pg.Rect((vertical_iterator+1)*75, 0, 2, self.display_height)
            pg.draw.rect(self.DISPLAY, (255, 0, 0), vertical_rect)

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


field = f.Field(3, 7)
game = Game(field)

# field = f.Field(5, 5)
# game = Game(field)
# game.field.place_bombs((1, 1), (3, 3))
# game.click_tile(2, 2)
# game.field.show()
