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
        """
        Add a Snake object to the game.

        Args:
            snake (Snake): The snake instance to add.

        Responsibilities:
            - Appends the given Snake object to self.snakes.
            - This allows the GameManager to keep track of all active snakes in the game.
            - By maintaining this list, GameManager can later update, move, or remove snakes
              as part of the game loop.
        """
        self.snakes.append(snake)

    def get_cell(self, pos):
        """
        Retrieve the Cell object at a specific board coordinate.

        Args:
            pos (tuple[int, int]): (x, y) grid coordinates of the desired cell.
                                   Example: (5, 7) refers to column 5, row 7.

        Returns:
            Cell | None: The Cell object at the given coordinate, or None if the coordinate
                         is invalid (outside the board dimensions).

        Behavior:
            - If pos is within the valid range (0 <= x,y < size), return self.cells[x][y].
            - If pos is out of range, return None.
            - This method acts as a safe accessor, preventing index errors when snakes
              or the game logic try to access out-of-bound cells.
        """
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        """
        Remove a snake from the game when it dies.

        Args:
            killed_snake (Snake): The snake object that should be removed.

        Responsibilities:
            - Removes the given snake from self.snakes.
            - Once removed, the snake will no longer be considered in game updates.
            - This is typically called when a snake collides with a wall, an obstacle,
              another snake, or itself.
        """
        self.snakes.remove(killed_snake)

    def get_next_fruit_pos(self):
        """
        Determine the optimal position for placing the next fruit on the board.

        Returns:
            tuple[int, int]: Coordinates (x, y) of the chosen cell for the next fruit.

        Algorithm:
            1. Iterate over all cells of the board.
            2. For each candidate cell (i, j):
               - If the cell is empty (background color), calculate its Manhattan distance
                 to all non-empty cells (cells that are not background: snake bodies,
                 other fruits, or obstacles).
               - Manhattan distance between (x1, y1) and (x2, y2) is:
                     |x1 - x2| + |y1 - y2|
               - Track the *minimum* distance from this cell to any non-empty cell.
            3. Among all empty cells, choose the one with the *maximum* of these minimum
               distances. In other words:
               - Find the empty cell that is furthest away from the nearest non-empty cell.
               - This ensures the fruit is placed in a challenging location, away from
                 existing objects.
            4. Return the coordinates of that cell.

        Notes:
            - If multiple cells have the same maximum minimum distance, the first one
              encountered in iteration order is selected.
            - This method ensures that fruits are not clustered near snakes or obstacles,
              increasing gameplay variety and difficulty.
        """
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int(abs(x - i) + abs(y - j)))

                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

