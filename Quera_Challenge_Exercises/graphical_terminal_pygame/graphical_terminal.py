import pygame


border_size = 1
border_color = (0, 0, 0)

command_registry = {}
def command(name: str):
    def decorator(func):
        command_registry[name] = func
        return func
    return decorator

pygame.init()
screen = pygame.display.set_mode((300, 300))
white = (255, 255, 255)
screen.fill(white)
pygame.display.update()

@command("change size")
def change_size(size):
    global border_size
    border_size = size

@command("change color")
def change_color(r: int, g: int, b: int):
    global border_color
    border_color = (r, g, b)

@command("draw line")
def draw_line(a: int,b: int,c: int,d: int):
    pygame.draw.line(screen,border_color,(a,b),(c,d), border_size)
    pygame.display.update()

@command("draw circle")
def draw_circle(x, g, r):
    pygame.draw.circle(screen,border_color,(x,g),r, border_size)
    pygame.display.update()

@command("draw polygon")
def draw_polygon(*num):
    points = [(num[i], num[i+1] ) for i in range(0, len(num), 2)]
    pygame.draw.polygon(screen,border_color,points,border_size)
    pygame.display.update()

@command("end drawing")
def end_drawing():
    pygame.image.save(screen, "draw.png")
    return True

def handle_command(user_line: str):
    user_line = user_line.strip()
    if not user_line:
        return None
    parts = user_line.split(" ")
    command_name = " ".join(parts[:2]).lower()
    args = parts[2:]
    func = command_registry.get(command_name)
    if func is None:
        return None
    try:
        numeric_args = list(map(int, args))
    except ValueError:
        return None

    try:
        return func(*numeric_args)
    except TypeError:
        return None


while True:
    pygame.event.pump()

    line_ =  input()
    stop = handle_command(line_)
    if stop:
        pygame.display.quit()
        pygame.quit()
        break