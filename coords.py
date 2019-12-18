def get_neighbor_coords(x, y):
    coords = dict()
    coords['top left'] = (x-1, y-1)
    coords['top'] = (x, y-1)
    coords['top right'] = (x+1, y-1)
    coords['left'] = (x-1, y)
    coords['right'] = (x+1, y)
    coords['bot left'] = (x-1, y+1)
    coords['bot'] = (x, y+1)
    coords['bot right'] = (x+1, y+1)
    return coords
