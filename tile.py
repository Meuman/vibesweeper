import pygame as pg


class Tile:
    def __init__(self, value, state, x=0, y=0):
        self._value = value
        self.state = state  # R - revealed, F - flag, H - hidden
        self.square = pg.Rect(x, y, 75, 75)

    def __add__(self, num):
        self._value += num
        return Tile(self._value, self.state)

    def __str__(self):
        if self.state == 'R':
            return str(self._value)
        else:
            return str(self.state)

    def reveal(self):
        self.state = 'R'

    def flag(self):
        self.state = 'F'

    def show(self):
        if self.state == 'R':
            return self._value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value
