import json


# Load configuration file
f = open("config.json")
data = json.loads(f.read())
f.close()

# === Game Board & Screen Settings ===
back_color = data['back_color']  # RGB list [R, G, B] → background color of the game screen
fruit_color = data['fruit_color']  # RGB list → color of the fruit block
block_color = data['block_color']  # RGB list → color of obstacles (houses/blocked cells)
cell_size = data['cell_size']  # Pixel size of each cell (square) on the game board
block_cells = data['block_cells']  # List of [x, y] coordinates marking blocked cells (obstacles)
table_size = data['table_size']  # Number of cells per row/column (board is always square)
height = data['height']  # Height of the entire game screen in pixels
width = data['width']  # Width of the entire game screen in pixels
sx = data['sx']  # Horizontal offset (pixels) of the game board from the left edge of the screen
sy = data['sy']  # Vertical offset (pixels) of the game board from the top edge of the screen

# === Snake(s) Settings ===
snakes = data['snakes']
"""
Each element in `snakes` represents one player’s snake, containing:

- keys: A dictionary mapping movement directions to keyboard keys:
    Example:
    "keys": {
        "UP": "w",
        "DOWN": "s",
        "LEFT": "a",
        "RIGHT": "d"
    }
    → 'w' = up, 's' = down, 'a' = left, 'd' = right

- sx: Initial horizontal position (x) of the snake’s head on the grid.
- sy: Initial vertical position (y) of the snake’s head on the grid.
- color: RGB list specifying the snake’s body color.
- direction: Initial movement direction ("UP", "DOWN", "LEFT", "RIGHT").
"""

# === Table Position on Screen ===