import consts

from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        """
        Constructor for the GameManager class.

        Args:
            size (int): The number of cells per row/column of the game board (board is size x size).
            screen (pygame.Surface): The surface on which the game is drawn.
            sx (int): Horizontal offset in pixels from the left edge of the screen.
            sy (int): Vertical offset in pixels from the top edge of the screen.
            block_cells (list[tuple[int,int]]): List of coordinates for blocked cells (obstacles),
                                                provided in config.json.
        """

        # --- Store basic configuration ---
        self.screen = screen       # The Pygame surface to draw on
        self.size = size           # Board dimension: number of cells per row/column
        self.cells = []            # 2D list of Cell objects (grid)
        self.sx = sx               # Horizontal pixel offset for the board
        self.sy = sy               # Vertical pixel offset for the board
        self.snakes = list()       # List of Snake objects in the game (initially empty)
        self.turn = 0              # Turn counter: counts how many steps have passed in the game

        # --- Build the grid of Cell objects ---
        # The board is size x size.
        # Each Cell is drawn at pixel coordinates:
        #   x = sx + i * cell_size
        #   y = sy + j * cell_size
        # This converts grid coordinates (i,j) into pixel coordinates on the screen.
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(
                    Cell(screen,
                         sx + i * consts.cell_size,
                         sy + j * consts.cell_size)
                )
            self.cells.append(tmp)

        # --- Place obstacles (blocked cells) ---
        # The coordinates from block_cells are given in grid units.
        # For each blocked cell, retrieve the corresponding Cell object
        # and set its color to block_color so it is drawn as an obstacle.
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)

    def get_next_fruit_pos(self): # returns tuple (x, y) that is the fruit location
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int( abs(x-i) + abs(y-j) ))


                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

    def handle(self, keys):
        pass
