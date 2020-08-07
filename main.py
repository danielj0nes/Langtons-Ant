"""Langton's Ant - Daniel Jones"""
import pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SCALE = 10
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Langton's Ant")
rows = int(WINDOW_WIDTH / SCALE)
columns = int(WINDOW_HEIGHT / SCALE)
board = [[[0, 0] for x in range(columns)] for y in range(rows)]  # [ant_enabled, tile_state]
orientation = 2
generation = 0
board[rows // 2][columns // 2] = [1, 0]  # Starting position (middle of screen)


def orient(o):
    states = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
    return states[o]


def parse():
    global board, orientation, generation
    ns = [[[0, 0] for x in range(columns)] for y in range(rows)]
    for x in range(rows):
        for y in range(columns):
            pos_x = x * SCALE
            pos_y = y * SCALE
            ant_enabled = board[x][y][0]
            tile_state = board[x][y][1]
            if ant_enabled:
                pygame.draw.rect(SCREEN, RED, [pos_x, pos_y, SCALE - 1, SCALE - 1])
                if tile_state:
                    orientation -= 1
                    if orientation < 0:
                        orientation = 3
                    ns[x][y][1] = 0
                    ns[(x + orient(orientation)[0] + rows) % rows][(y + orient(orientation)[1] + columns) % columns][0] = 1
                else:
                    orientation += 1
                    if orientation == 4:
                        orientation = 0
                    ns[x][y][1] = 1
                    ns[(x + orient(orientation)[0] + rows) % rows][(y + orient(orientation)[1] + columns) % columns][0] = 1
            else:
                pygame.draw.rect(SCREEN, WHITE, [pos_x, pos_y, SCALE - 1, SCALE - 1])
                if tile_state:
                    ns[x][y][1] = 1
                    pygame.draw.rect(SCREEN, BLACK, [pos_x, pos_y, SCALE - 1, SCALE - 1])
    board = ns
    generation += 1
    print(generation)


pygame.init()
while True:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    parse()
    pygame.display.update()
