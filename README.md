# *VIBESWEEPER*
##### Mateusz Przeździecki, 2020
### A little about the game
I'm fairly certain all of us have already played minesweeper at least once in their lifetime, so I'm going to go over the rules very briefly.

VIBESWEEPER works pretty much like your normal minesweeper game: You click tiles, the tile's number show how many bombs are in adjacent tiles, and based on that information you try try to reveal every tile that doesn't have a bomb one it.

The only difference between a normal minesweeper game and VIBESWEEPER is the creepy smiley face that patiently waits for a brief gap in your defense and attack you. To not be attacked by the VIBE MAN you must reveal the tiles without bombs. After you do so, VIBE MAN seems like a pretty chill dude and everything is alright.

## External libraries
The only external library that is used in the program is the PyGame library. It allows the game to be rendered like a normal minesweeper game would.

## Structure of the program and modules
The basic game depends on a few modules. These are:
- The tile module
- The field module
- The game module

Modules like ranfieldgen and coords are also used by the game, but their purpose is to increase the quality of life (quality of game?) for the player, for example: ensuring that the first click on a random map won't end the game instantly, as that is not much fun.

## The tile module
### Attributes
The tile module contains the tile class and other methods that change the state of a tile.
The attributes of a tile are:
- Value (An integer from 0 to 9)
  * represents how many bombs are in neighboring tiles, and if the value is equal to 9, it means that there is a bomb on the tile.
- State (One of the letters: 'H', 'R' or 'F')
  * H means that the tile is hidden.
  * R means that the tile is revealed.
  * F means that the tile is flagged.
- X and Y
  *Two integers representing the coordinates on the board.
### Functions and methods
The module also contains many self-explanatory functions such as is_hidden(), show(), flag(), etc. which I am not going to comment on.

## The field module
### Attributes
The field module contains the field class and other methods that can manipulate the field.
The field itself is a two-dimensional array filled with tiles.
The attributes of a field are:
- Rows and columns,
  * both integers which signify the dimensions of the array.
- Two_dim_field 
  - the most important part of the class: it is the two dimensional array of tiles.
- Default_state
  * An attribute that controls the default state of the tile (hidden, flagged, etc.). Used mostly for debugging.
### Functions and methods
#### place_bombs
This function takes tuples as its arguments: The tuples represent the coordinates of the tile.
We change the value of the given tile to a 9, and increase the value of the neighboring tiles by 1, unless the neighboring tiles are also a bomb.
### count_bombs
This function does not take any arguments. It iterates through the two_dim_field of the array and counts how many bombs there are.

## The ranfieldgen module
### Functions and methods
#### generate_random_field
This function takes 5 arguments: rows, columns, number of bombs, nobomb_x, and nobomb_y
The first three arguments are self-explanatory.

Nobomb_x and nobomb_y are the coordinates of the tile that was clicked as the first tile on the map.
As we do not want to lose instantly after clicking the first tile, we make a dictionary of the neighboring tiles to the tile that was clicked the earliest.

We take random coordinates: if we can place a bomb there (if the coordinates aren't in the dict or aren't the nobomb coordinates) we do so, and remove one from our bomb counter.
We continue until the bomb counter is equal to 0.

