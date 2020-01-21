import field as f
from coords import get_neighbor_coords
import pygame as pg
from ranfieldgen import generate_random_field


class Game:
    def __init__(self, field_rows=8, field_columns=8, num_of_bombs=9):
        pg.init()
        icon = pg.image.load('ico.png')
        pg.display.set_icon(icon)
        pg.display.set_caption("Vibesweeper")
        self.RECT_SIZE = 60
        self.NUMBER_X_ADJUSTMENT_RATE = 3.05
        self.NUMBER_Y_ADJUSTMENT_RATE = 1.2
        self.field = f.Field(field_rows, field_columns)
        self.result = None
        self.font = pg.font.SysFont(None, self.RECT_SIZE)
        self.init_color_dict()
        self.init_screen()
        self.init_menu()
        self.draw_tiles()
        # self.draw_borders()
        first_click = False
        while self.result is None:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.result = False
                mouse_pos = self.get_mouse_coords()
                click_state = pg.mouse.get_pressed()
                if click_state[0]:
                    if first_click is False:
                        self.field = generate_random_field(field_rows, field_columns, num_of_bombs, mouse_pos[0], mouse_pos[1])
                        self.threebv = self.calculate_3bv()
                        print(self.threebv)
                        first_click = True
                    self.click_tile(mouse_pos[0], mouse_pos[1])
                if click_state[2]:
                    if self.field.two_dim_field[mouse_pos[0]][mouse_pos[1]].is_hidden():
                        self.field.two_dim_field[mouse_pos[0]][mouse_pos[1]].flag()
                    elif self.field.two_dim_field[mouse_pos[0]][mouse_pos[1]].is_flagged():
                        self.field.two_dim_field[mouse_pos[0]][mouse_pos[1]].unflag()
                self.draw_tiles()
                pg.display.update()

    def init_screen(self):
        self.display_width = self.field.x_limit*self.RECT_SIZE
        self.display_height = (self.field.y_limit + 1)*self.RECT_SIZE
        self.DISPLAY = pg.display.set_mode((self.display_width, self.display_height))

    def init_menu(self):
        menurect = pg.Rect(0, 0, self.display_width, self.RECT_SIZE)
        pg.draw.rect(self.DISPLAY, (200, 200, 200), menurect)
        self.vibe_man = pg.image.load('him.png')
        self.vibe_man = pg.transform.smoothscale(self.vibe_man, (self.RECT_SIZE, self.RECT_SIZE))
        self.DISPLAY.blit(self.vibe_man, (self.display_width//2 - self.RECT_SIZE//2, 0))
        self.bomb = pg.image.load('bomb.png')
        self.bomb = pg.transform.smoothscale(self.bomb, (self.RECT_SIZE, self.RECT_SIZE))

    def draw_tiles(self):
        field = self.field.two_dim_field
        flag = pg.image.load('flag.png')
        flag = pg.transform.smoothscale(flag, (self.RECT_SIZE, self.RECT_SIZE))
        for rows in range(self.field.y_limit):
            for columns in range(self.field.x_limit):
                rect_to_draw = pg.Rect(columns*(self.RECT_SIZE), self.RECT_SIZE + rows*(self.RECT_SIZE), self.RECT_SIZE, self.RECT_SIZE)  # create the rect to draw
                tile_value = field[columns][rows].get_value()
                value_to_draw = self.font.render(str(tile_value), True, self.color_dict[tile_value])
                if field[columns][rows].is_hidden():  # render hidden tile
                    pg.draw.rect(self.DISPLAY, (175, 175, 175), rect_to_draw)
                elif field[columns][rows].is_flagged():
                    pg.draw.rect(self.DISPLAY, (175, 175, 175), rect_to_draw)
                    self.DISPLAY.blit(flag, (columns*self.RECT_SIZE, int(self.RECT_SIZE) + rows*self.RECT_SIZE))
                elif field[columns][rows].is_revealed():  # render revealed tile
                    pg.draw.rect(self.DISPLAY, (125, 125, 125), rect_to_draw)
                    if tile_value != 0 and tile_value != 9:
                        self.DISPLAY.blit(value_to_draw, (columns*self.RECT_SIZE + self.RECT_SIZE//self.NUMBER_X_ADJUSTMENT_RATE, int(self.RECT_SIZE*self.NUMBER_Y_ADJUSTMENT_RATE) + rows*self.RECT_SIZE))
                    if tile_value == 9:
                        self.DISPLAY.blit(self.bomb, (columns*self.RECT_SIZE, int(self.RECT_SIZE) + rows*self.RECT_SIZE))
                pg.draw.rect(self.DISPLAY, (75, 75, 75), rect_to_draw, 1)  # draw the border around the rectangle

    def click_tile(self, x, y, field=None):
        if field is None:
            field = self.field
        if x < 0 or y < 0:  # if the given x and y are not correct do nothing
            return
        try:
            if field.two_dim_field[x][y].is_flagged() or field.two_dim_field[x][y].is_revealed():  # if the clicked tile is flagged or revealed do nothing
                return
            field.two_dim_field[x][y].reveal()  # reveal the clicked tile
            if field.two_dim_field[x][y].get_value() == 9:  # if the clicked tile is a bomb lose the game
                self.result = False
                return
            elif field.two_dim_field[x][y].get_value() == 0:  # if the clicked tile has a value equal to 0 reveal it and the surrounding ones
                self.reveal_surrounding_tiles(x, y, field)
        except Exception:
            return

    def reveal_surrounding_tiles(self, x, y, field=None):
        if field is None:
            field = self.field
        neighbor_coords = get_neighbor_coords(x, y)
        for coords in neighbor_coords:
            try:
                processed_tile = field.two_dim_field[coords[0]][coords[1]]
                if processed_tile.is_hidden() and processed_tile.get_value() != 9:
                    self.click_tile(coords[0], coords[1])
            except Exception:
                pass

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
            9: (255, 255, 255),
            'H': (175, 175, 175),
            'F': (175, 175, 175),
            'R': (125, 125, 125)
        }

    def calculate_3bv(self):
        clicks = 0
        calculation_field = f.Field(self.field)  # copy by value
        for y in range(calculation_field.y_limit):  # first iteration, click all zeroes
            for x in range(calculation_field.x_limit):
                if calculation_field.two_dim_field[x][y].get_value == 0:
                    self.click_tile(x, y, calculation_field)
                    clicks += 1
        for y in range(calculation_field.y_limit):
            for x in range(calculation_field.x_limit):
                if calculation_field.two_dim_field[x][y].get_value != 9:
                    self.click_tile(x, y, calculation_field)
                    clicks += 1
        return clicks


# field = f.Field(5, 5)
# field.place_bombs((1, 1), (2, 2), (3, 4), (4, 4), (2, 1))
# field.show()
game = Game()
