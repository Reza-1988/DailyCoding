import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.width = 640
        self.height = 480
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.speed = [1, 1]
        self.black = (0, 0, 0)
        self.ball, self.ballrect = self.load_image("sq.png")

    @staticmethod
    def load_image(image_name: str):
        img = pygame.image.load(image_name)
        rect = img.get_rect()
        return img, rect

    def move_ball(self) -> None:
        new_rect = self.ballrect.move(self.speed)

        if new_rect.left < 0 or new_rect.right > self.width:
            self.speed[0] *= -1
        if new_rect.top < 0 or new_rect.bottom > self.height:
            self.speed[1] *= -1
        self.ballrect = self.ballrect.move(self.speed)

    def draw(self) -> None:
        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()


    @staticmethod
    def handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



g = Game()

while True:
    g.handle_events()
    g.move_ball()
    g.draw()
