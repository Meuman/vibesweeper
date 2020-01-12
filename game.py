import field as f
from coords import get_neighbor_coords
import pygame as pg


class Game:
    def __init__(self, field=f.Field(5, 5)):
        pg.init()
        icon = pg.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\ico.png')
        pg.display.set_icon(icon)
        pg.display.set_caption("Vibesweeper")
        self.RECT_SIZE = 60
        self.field = field
        self.result = None
        self.font = pg.font.SysFont(None, self.RECT_SIZE)
        self.init_color_dict()
        self.init_screen()
        self.init_menu()
        self.draw_tiles()
        # self.draw_borders()
        pg.display.update()
        while self.result is None:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.result = False
                mouse_pos = self.get_mouse_coords()
                print(mouse_pos)
                click_state = pg.mouse.get_pressed()
                if click_state[0]:
                    self.click_tile(mouse_pos[0], mouse_pos[1])
                if click_state[1]:
                    self.field.two_dim_field[mouse_pos[0]][mouse_pos[1]].flag()
                self.draw_tiles()
                pg.display.update()

    def init_screen(self):
        self.display_width = self.field.x_limit*self.RECT_SIZE
        self.display_height = (self.field.y_limit + 1)*self.RECT_SIZE
        self.DISPLAY = pg.display.set_mode((self.display_width, self.display_height))

    def init_menu(self):
        menurect = pg.Rect(0, 0, self.display_width, self.RECT_SIZE)
        pg.draw.rect(self.DISPLAY, (200, 200, 200), menurect)
        self.vibe_man = pg.image.load('C:\\Users\\derpi\\Documents\\GitHub\\minesweeper\\him.png')
        self.vibe_man = pg.transform.smoothscale(self.vibe_man, (self.RECT_SIZE, self.RECT_SIZE))
        self.DISPLAY.blit(self.vibe_man, (self.display_width//2 - self.RECT_SIZE//2, 0))

    # def draw_borders(self):
    #     horizontal_range = self.field.y_limit
    #     vertical_range = self.field.x_limit
    #     for horizontal_iterator in range(horizontal_range):
    #         horizontal_rect = pg.Rect(0, (horizontal_iterator+1)*self.RECT_SIZE, self.display_width, 1)
    #         pg.draw.rect(self.DISPLAY, (0, 0, 0), horizontal_rect)
    #     for vertical_iterator in range(vertical_range):
    #         vertical_rect = pg.Rect((vertical_iterator+1)*self.RECT_SIZE, 0, 1, self.display_height)
    #         pg.draw.rect(self.DISPLAY, (0, 0, 0), vertical_rect)

    def draw_tiles(self):
        field = self.field.two_dim_field
        for rows in range(self.field.y_limit):
            for columns in range(self.field.x_limit):
                rect_to_draw = pg.Rect(columns*(self.RECT_SIZE), self.RECT_SIZE + rows*(self.RECT_SIZE), self.RECT_SIZE, self.RECT_SIZE)
                tile_value = field[columns][rows].get_value()
                value_to_draw = self.font.render(str(tile_value), True, self.color_dict[tile_value])
                if field[columns][rows].state == 'H':
                    pg.draw.rect(self.DISPLAY, (175, 175, 175), rect_to_draw)
                if field[columns][rows].state == 'R':
                    pg.draw.rect(self.DISPLAY, (125, 125, 125), rect_to_draw)
                    if tile_value != 0 and tile_value != 9:
                        self.DISPLAY.blit(value_to_draw, (columns*self.RECT_SIZE + self.RECT_SIZE//3.05, int(self.RECT_SIZE*1.2) + rows*self.RECT_SIZE))
                    if tile_value == 9:
                        self.DISPLAY.blit(self.vibe_man, (columns*self.RECT_SIZE, int(self.RECT_SIZE) + rows*self.RECT_SIZE))
                pg.draw.rect(self.DISPLAY, (75, 75, 75), rect_to_draw, 1)

    def click_tile(self, x, y):
        if x < 0 or y < 0:  # if the given x and y are not correct do nothing
            return
        try:
            if self.field.two_dim_field[x][y].state == 'F':  # if the clicked tile is flagged do nothing
                return
            self.field.two_dim_field[x][y].reveal()
            if self.field.two_dim_field[x][y].get_value() == 9:  # if the clicked tile is a bomb lose the game
                self.result = False
                return
            if self.field.two_dim_field[x][y].get_value() == 0:  # if the clicked tile has a value equal to 0 reveal it and the surrounding ones
                self.reveal_surrounding_tiles(x, y)
        except Exception:
            return

    def reveal_surrounding_tiles(self, x, y):
        neighbor_coords = get_neighbor_coords(x, y)
        for coords in neighbor_coords.values():
            try:
                processed_tile = self.field.two_dim_field[coords[0]][coords[1]]
                if processed_tile == 'H':
                    if processed_tile.get_value() != 9:
                        processed_tile.reveal()
                        if processed_tile.get_value() == 0:
                            self.reveal_surrounding_tiles(coords[0], coords[1])
            except Exception:
                return

    def get_mouse_coords(self):
        position = pg.mouse.get_pos()
        x = position[0]//self.RECT_SIZE
        y = position[1]//self.RECT_SIZE
        return (x, y-1)

    def init_color_dict(self):
        self.color_dict = {
            0: (125, 125, 125),
            1: (0, 0, 253),
            2: (1, 126, 2),
            3: (255, 0, 1),
            4: (1, 1, 128),
            5: (127, 3, 0),
            6: (0, 129, 128),
            7: (0, 0, 0),
            8: (102, 0, 102),
            9: (255, 255, 255)
        }

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


field = f.Field(5, 5)
field.place_bombs((1, 1), (2, 2), (3, 4), (4, 4), (2, 1))
field.show()
game = Game(field)
game.field.show()

# field = f.Field(5, 5)
# game = Game(field)
# game.field.place_bombs((1, 1), (3, 3))
# game.click_tile(2, 2)
# game.field.show()
