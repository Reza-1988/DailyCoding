import pygame, consts, sys
from game_manager import GameManager
from snake import Snake


def main():
    pygame.init()

    # Create the game screen using values defined in consts.py
    screen = pygame.display.set_mode((consts.height, consts.width))
    screen.fill(consts.back_color)

    # Initialize the GameManager (handles the overall game logic and flow)
    game = GameManager(consts.table_size, screen, consts.sx, consts.sy, consts.block_cells)

    # Create Snake objects (one per player) using configuration from consts.py
    snakes = list()
    for snake in consts.snakes:
        print(snake)
        snakes.append(
            Snake(snake['keys'], game, (snake['sx'], snake['sy']), snake['color'], snake['direction'])
        )

    # Main game loop:
    # - Capture user input (keyboard events, quit event)
    # - Send pressed keys to GameManager for state updates
    # - Control frame rate with a short delay
    while True:
        events = pygame.event.get()
        keys = []
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.append(event.unicode)

        game.handle(keys)

        # Small delay to regulate game speed (frame rate control)
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
