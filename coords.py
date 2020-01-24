def get_neighbor_coords(x, y):
    coords = set()
    coords.add((x-1, y-1))  # top left
    coords.add((x, y-1))  # top
    coords.add((x+1, y-1))  # top right
    coords.add((x-1, y))  # left
    coords.add((x+1, y))  # right
    coords.add((x-1, y+1))  # bot left
    coords.add((x, y+1))  # bot
    coords.add((x+1, y+1))  # bot right
    return coords
