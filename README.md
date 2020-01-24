# *VIBESWEEPER*
## *DOCUMENTATION*
##### Mateusz Przeździecki, 2020
## A little about the game
I'm fairly certain all of us have already played minesweeper at least once in their lifetime, so I'm going to go over the rules very briefly.

VIBESWEEPER works pretty much like your normal minesweeper game: You click tiles, the tile's number show how many bombs are in adjacent tiles, and based on that information you try try to reveal every tile that doesn't have a bomb one it.

The only difference between a normal minesweeper game and VIBESWEEPER is the creepy smiley face that patiently waits for a brief gap in your defense and attack you. To not be attacked by the VIBE MAN you must reveal the tiles without bombs. After you do so, VIBE MAN seems like a pretty chill dude and everything is alright.

## External libraries
The only external library that is used in the program is the PyGame library. It allows the game to be rendered like a normal minesweeper game would.

## How to play the game? How to use the vibesweeper.py file?
### The vibesweeper.py file has three modes.
*  Mode no. 0: Generate a random map based on the given values and play on it.
* Mode no. 1: Play on a given map in a .txt file
* Mode no.2 Generate a random map based on the given values, and save it to a .txt file.
<code> vibesweeper.py mode rows_or_field_path columns num_of_bombs output_path </code>
In Mode 0, the output_path argument must be ignored.
In mode 1, all arguments other than rows_or_field_path must be ignored.
### Examples
1:
	Let's say we want to play on a randomly generated map, 10 by 10, which has 20 bombs.
	To launch the it, we have to type this into the terminal:
	<code> vibesweeper.py 0 10 10 20 </code>

2: Let's say we want have a map file coolest_map_ever.txt in the same folder as our minesweeper.py folder and we want to play on it.
To do so, we type:
<code> vibesweeper.py 1 "coolest_map_ever.txt" </code>

3: Let's say that we want to have new generated map with given dimensions and number of bombs in a my_new_map.txt file.
10 rows, 10 columns, 10 bombs.
To do so, we type:
<code> vibesweeper.py 2 10 10 "my_new_map.txt" </code>




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

## The coords module
### Functions and methods
#### get_neighbor_coords
This function takes coordinates as its arguments. It returns a set of all the neigboring tile coordinates.

## The game module
### Before we begin
This module is pretty much the core of the entire game (200+ lines of code!). The entire gameplay, graphics and all necessary calculations are done there. I am aware that it would be better to split this module into three different ones, but due to time constraints I have to leave it as it is. 
### Attributes
* Mode
 * Mode 0 means that we do not have a preset map and wish to generate one.
 * Mode 1 means that we have a preset map and wish to play on it.
The rest of the arguments are self-explanatory.
### Functions and methods
#### init_pygame
Self explanatory, initializes the pygame library and and minor things such as the icon and the program name in the taskbar.

#### init_constants
In this function we declare the constant values used in the program. Rect_size stands for the dimensions of the rectangles which represent a tile, and the other two are magic numbers, which are used to make sure the number on a revealed tile is centered.

#### init_screen
In this function we set the display width and height based on the dimensions of the field.

#### init_menu
In this function we declare all entities to render the menu properly.
We also load the bomb image and the VIBE MAN image.

#### maintain_menu
In this function we update the menu to show and update dynamic data, for example the number of flags left, the state of the game, etc.

#### draw_tiles_for_ending
This function is used when the game has ended. If the player has won, it shows the pretty chill version of VIBE MAN. Otherwise, it shows a hungry VIBE MAN attacking the player. 
If the tile was flagged incorrectly, put a red cross on the flag.
If the tile was a bomb tile, show the bomb image on that tile.

#### click_tile
This function takes x and y coordinates as its arguments. If the targeted tile is flagged, it is unclickable, and the function ends.
If the targeted tile is hidden, reveal it.
* If the tile was a bomb, set the game result to False and return from the function
* If the tile was a non-zero and non-bomb tile, reveal it
* If the tile was a zero tile, reveal it AND its surrounding tiles. If one of the surrounding tiles is also a zero tile, reveal its surroundings. If one of its surrounding... (and so on. This uses recursion.)
#### reveal_surrounding_tiles
This function takes x and y coordinates as its arguments. We reveal the surrounding tiles of the tile with the given coordinates, 

#### get_mouse_coords
This function gets the mouse coordinates and gives exact field coordinates corresponding to the mouse position by dividing the coordinates by the constant RECT_SIZE.

#### init_color_dict
This function creates a dictionary which assigns colors to states and numerical values of tiles. 

### calculate_3bv
This function creates a deep copy of the two_dim_field of our map.
If iterates through the map two times:
* The first time it clicks all the zero tiles, revealing them and their surrounding tiles
* The second time it clicks all non-zero tiles.
It counts the clicks, and once all non-bomb tiles have been revealed, 

## The map_parser module
### Functions and methods
This module has functions needed to convert a map into a .txt file, and a .txt file into a map.
The maps must be written in this way:
* If the tile is a bomb, write B or b on its coordinate.
* If the tile is not a bomb, write . on its coordinate.
The dimensions of the map must be larger than 8x8.
The map must have 1 or more bombs.
Although, due to how the random map generation works, the following equation must also be true.
rows*columns - bombs >= 9
#### text_to_map
This method takes a .txt file and returns a Field object based on how the .txt file was written.
### map_to_text
This method takes a field object and a path to the file.
It opens the file from the path and writes a map into that file.

### Special thanks
Special thanks to subduedhues for the vibe man emoji art.
