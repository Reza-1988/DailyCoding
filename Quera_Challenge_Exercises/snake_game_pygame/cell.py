import pygame, consts

# This module defines the Cell class.
# Each square (cell) of the game board is represented by a Cell instance.
# The *type* of a cell (empty, fruit, snake, blocked) is inferred from its color.

class Cell:
    def __init__(self, surface, sx, sy, color=consts.back_color):
        """
        Initialize a single board cell and draw it on the given surface.

        Args:
            surface (pygame.Surface): The surface (e.g., the game screen) to draw on.
            sx (int): X coordinate (in pixels) of the cell's top-left corner on the surface.
            sy (int): Y coordinate (in pixels) of the cell's top-left corner on the surface.
            color (tuple[int, int, int], optional): Initial fill color (RGB). Defaults to consts.back_color.

        Behavior:
            - Stores position (sx, sy), size (from consts.cell_size), surface, and color.
            - Draws a 1-pixel black border rectangle for the cell’s outline.
            - Fills the interior of the cell with the initial color via set_color().
        """
        self.sx = sx
        self.sy = sy
        self.size = consts.cell_size
        self.surface = surface
        self.color = color

        # Draw the cell border (outline only) as a 1-pixel black rectangle.
        # Rect format: (x, y, width, height); the last arg '1' means "only border, 1 px thick".
        pygame.draw.rect(surface, (0, 0, 0), (sx, sy, self.size, self.size), 1)

        # Fill the inside area with the initial color.
        self.set_color(color)

    def set_color(self, color):
        """
        Fill the cell's interior (inside the border) with the given color and update the display.

        Why the +1 and -2 offsets?
            - We drew a 1-pixel border for the cell at (sx, sy) with size (size, size).
            - To avoid painting over that border, we inset the fill rectangle by 1 pixel on each side:
                * left/top starts at (sx + 1, sy + 1)
                * width/height are reduced by 2 (1 px from each side): (size - 2, size - 2)
            - This preserves the border and cleanly fills the inner area only.

        Args:
            color (tuple[int, int, int]): New fill color (RGB).
        """
        self.color = color

        # Draw the inner (filled) rectangle, inset by 1 px on all sides to preserve the border.
        # Rect is: top-left (sx+1, sy+1) and size (size-2, size-2).
        pygame.draw.rect(
            self.surface,
            color,
            (self.sx + 1, self.sy + 1, self.size - 2, self.size - 2)
        )

        # Push the updated drawing to the screen.
        pygame.display.update()
