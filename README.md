# Minesweeper
This is the classic minesweeper game implemented in python and using pygame for computer graphics and achieving the nostalgic feel of the classic game.

The game starts a 10x10 board with 10 bombs distributed randomly and 10 flags to be planted, the game is started with the command line "python3 minesweeper_game.py".


### How to Play
Minesweeper is a single-player logic-based computer game with the objective of locating a predetermined number of bombs placed around the board in cells. 

For each cell that does not hold a bomb, a number is placed, this number represents the number of bombs neighboring the cell, where "neighboring" is defined as cells that share the same border on one of the four sides of the cell or share the same corner, meaning each cell can have at most 8 neighbors: Two horizontal neighbors (left and right), two vertical neighbors (top and bottom) and four diagonal neighbors (top left, top right, bottom left, bottom right).

For each cell that has no neighboring bombs i.e. its value is 0, the cell is just empty (no number placed).

The game starts with all cells unrevealed/hidden, you have the choice to dig (left mouse click) any cell. 
- If you dig in a bomb cell, it is game over.
- If you dig over a cell that is not a bomb, it is revealed i.e. the number will be shown.
- If you dig over a cell with a value of 0, the game reveals the cell as well as all its neighbors recursively until it encounters cell number (> 0) on each side.

You can right click any unrevealed cell to plant a flag which can help you determine where bombs are placed (supposedly); right clicking a flagged cell will unflag it.

The game is won when you reveal all non-bomb cells and all bomb cells are intact.


## User Stories
User can left click any unrevealed cell to dig/reveal it, if the cell choosen is a bomb, it is game over.

User can right click any unrevealed cell to plant a flag (with a max of 10 flags planted).

User can always see the number of bombs left to be flagged.

User can restart game at any point using the "New Game" button.

## Screen
The dark gray cells represents revealed (dug) cells which have no neighboring bombs, white cells are revealed (dug) cells and light gray cells are unrevealed (undug).
![minesweeper](https://github.com/LaraKinan/Minesweeper/assets/102249800/b074fdd6-bec6-4cd7-8634-f6c34eaee6f7)
