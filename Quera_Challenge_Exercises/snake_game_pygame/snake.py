import consts


# This class is responsible for managing the behavior and state of each snake in the game.
# Each Snake object knows its own body cells, direction, color, and control keys.
# It also interacts with the GameManager to register itself and update the game board.

class Snake:
    # Direction mappings:
    # dx and dy define how the snake's head position changes based on the movement direction.
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        """
        Constructor for the Snake class.

        :param keys: A dictionary specifying the snake's control keys.
                     Example format (from config.json):
                     {
                         "UP": "w",
                         "DOWN": "s",
                         "LEFT": "a",
                         "RIGHT": "d"
                     }

        :param game: The GameManager object that manages the game state.
                     The snake will register itself with this manager.

        :param pos: A tuple (x, y) representing the initial position of the snake’s head on the grid.
                    At the start of the game, the snake only consists of this one cell.

        :param color: Snake color as an RGB triple list (e.g., [255, 0, 0] for red).

        :param direction: The initial movement direction of the snake.
                          Must be one of "UP", "DOWN", "LEFT", or "RIGHT".

        Responsibilities of the constructor:
        - Store all input parameters as snake properties (keys, color, direction, etc.).
        - Create a list self.cells that stores all body cells of the snake in order.
          Initially, this list only contains one element: the head position.
          The last element of self.cells always represents the head.
        - Register this snake with the GameManager using add_snake().
        - Update the game board by coloring the starting cell with the snake’s color.
        """
        self.keys = keys
        self.cells = [pos]  # Body of the snake (list of coordinates), head is always the last element.
        self.game = game
        self.game.add_snake(self)  # Register the snake in the game manager.
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)  # Paint the initial head cell with the snake's color.

    def get_head(self):
        """
        Returns the coordinates of the snake's head.
        The head is always the last element in self.cells.
        """
        return self.cells[-1]

    def val(self, x):
        """
        Wraparound function for grid coordinates.

        :param x: A coordinate (row or column index) on the game board.
        :return: A valid coordinate adjusted for wraparound behavior.

        Behavior:
        - If x is negative (e.g., the snake moved left/up past the board edge),
          add game.size to wrap it around to the opposite side.
        - If x is greater than or equal to game.size (e.g., moved right/down past the edge),
          subtract game.size to wrap it back to the other side.
        - Otherwise, return x unchanged.

        This creates a toroidal ("donut-shaped") game board,
        where going off one edge makes the snake appear on the opposite edge.
        """
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        pass

    def handle(self, keys):
        """
        Handle direction changes for this frame based on pressed keys.

        Args:
            keys (list[str]): Characters pressed in this frame, e.g. ['a', 'd', 'w'].
                              Only the first *valid* control key should take effect.

        Logic:
            - Build an inverse mapping from the configured control keys to directions:
                  self.keys:  {'UP':'w','DOWN':'s','LEFT':'a','RIGHT':'d'}
                  dir_map:    {'w':'UP','s':'DOWN','a':'LEFT','d':'RIGHT'}
            - Iterate over the pressed keys in order (keys[0], keys[1], ...):
                * If a pressed key maps to a direction (via dir_map), consider it as candidate `new_dir`.
                * If `new_dir` is the exact opposite of the current direction, ignore it (no 180° turn).
                * Otherwise, accept it:
                    - set self.direction = new_dir
                    - break (apply only the first valid change this frame).

        Notes:
            - If no pressed key is valid (or all are opposite), direction remains unchanged.
            - This respects the "first valid key wins" requirement.
        """

        # Invert mapping: char -> direction (e.g., 'w' -> 'UP')
        dir_map = {v:k for k,v in self.keys.items()}
        for char in keys:
            # Only consider keys that are configured for this snake
            if char in dir_map:
                new_dir = dir_map[char]
                # Skip 180-degree turns (i.e., opposite directions).
                # Using class-level dx/dy ensures a reliable, data-driven check:
                # Opposite means the per-axis deltas sum to zero on both axes.
                if not(
                        (Snake.dx[new_dir] + Snake.dx[self.direction] == 0) and
                        (Snake.dy[new_dir] + Snake.dy[self.direction] == 0)
                ):
                    # First valid change takes effect; ignore any remaining keys this frame
                    self.direction = new_dir
                    break