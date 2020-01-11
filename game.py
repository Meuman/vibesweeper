import field as f
from coords import get_neighbor_coords
import pygame as pg


class Game:
    def __init__(self, field=f.Field(5, 5)):
        pg.init()
        icon = pg.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\ico.png')
        pg.display.set_icon(icon)
        pg.display.set_caption("Vibesweeper")
        self.RECT_SIZE = 250
        self.field = field
        self.result = None
        self.init_screen()
        self.draw_tiles()
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
        menurect = pg.Rect(0, 0, self.display_width, self.RECT_SIZE)
        pg.draw.rect(self.DISPLAY, (200, 200, 200), menurect)
        vibe_man = pg.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\him.png')
        vibe_man = pg.transform.smoothscale(vibe_man, (self.RECT_SIZE, self.RECT_SIZE))
        self.DISPLAY.blit(vibe_man, (self.display_width//2 - self.RECT_SIZE//2, 0))

    def draw_borders(self):
        horizontal_range = self.field.y_limit
        vertical_range = self.field.x_limit
        for horizontal_iterator in range(horizontal_range):
            horizontal_rect = pg.Rect(0, (horizontal_iterator+1)*self.RECT_SIZE, self.display_width, 1)
            pg.draw.rect(self.DISPLAY, (0, 0, 0), horizontal_rect)
        for vertical_iterator in range(vertical_range):
            vertical_rect = pg.Rect((vertical_iterator+1)*self.RECT_SIZE, 0, 1, self.display_height)
            pg.draw.rect(self.DISPLAY, (0, 0, 0), vertical_rect)

    def draw_tiles(self):
        field = self.field.two_dim_field
        for rows in range(self.field.y_limit):
            for columns in range(self.field.x_limit):
                rect_to_draw = pg.Rect(columns*(self.RECT_SIZE), self.RECT_SIZE + rows*(self.RECT_SIZE), self.RECT_SIZE, self.RECT_SIZE)
                if field[columns][rows].state == 'H':
                    pg.draw.rect(self.DISPLAY, (175, 175, 175), rect_to_draw)
                if field[columns][rows].state == 'R':
                    pg.draw.rect(self.DISPLAY, (125, 125, 125), rect_to_draw)

    def click_tile(self, x, y):
        x -= 1
        y -= 1
        try:
            self.field.two_dim_field[x][y].reveal()
            if self.field.two_dim_field[x][y].get_value() == 9:
                self.result = False
                return
            if self.field.two_dim_field[x][y].get_value() == 0:
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
                if processed_tile == 'H':
                    if processed_tile.get_value() != 9:
                        self.click_tile(coords[0], coords[1])
            except Exception:
                pass

    # def reveal_surrounding_tiles(self, x, y):
    #     x -= 1
    #     y -= 1
    #     neighbor_coords = get_neighbor_coords(x, y)
    #     for coords in neighbor_coords.values():
    #         try:
    #             processed_tile = self.field.two_dim_field[coords[0]][coords[1]]
    #             if processed_tile.state == 'H':
    #                 if processed_tile.get_value() != 9:
    #                     processed_tile.reveal()
    #                 if processed_tile.get_value() == 0:
    #                     self.reveal_surrounding_tiles(coords[0], coords[1])
    #         except Exception:
    #             pass


field = f.Field(6, 6)
game = Game(field)

# field = f.Field(5, 5)
# game = Game(field)
# game.field.place_bombs((1, 1), (3, 3))
# game.click_tile(2, 2)
# game.field.show()
