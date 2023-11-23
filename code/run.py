import pygame
import math
from setting_variables import *
from player import Player
from map import map, TITLE


def run():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(player_pos, player_angle, player_speed)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        moves(player)

        draw(window, player)

        pygame.display.flip()
        clock.tick(FPS)


def moves(player):
    player.move()


def draw(window, player):
    pygame.draw.rect(window, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(window, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    ray_casting(window, player.get_pos(), player.get_angle())
    # pygame.draw.circle(window, GREEN, player.pos, 12)
    # pygame.draw.line(window, GREEN, player.pos, (player.get_pos_x() + WIDTH * math.cos(player.get_angle()),
    #                                              player.get_pos_y() + WIDTH * math.sin(player.get_angle())))
    # for x, y in map:
    #     pygame.draw.rect(window, DARKGRAY, (x, y, TITLE, TITLE), 2)


def ray_casting(window, player_pos, player_angle):
    cur_angle = player_angle - PLAYER_FOV
    xo, yo = player_pos
    for ray in range(NUMBER_RAYS):
        sin_angle = math.sin(cur_angle)
        cos_angle = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_angle
            y = yo + depth * sin_angle

            if (x // TITLE * TITLE, y // TITLE * TITLE) in map:
                depth *= math.cos(player_angle - cur_angle)
                height = COOFIC / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(window, color, (ray * SCALE, HALF_HEIGHT - height // 2, SCALE, height))
                break
        cur_angle += DELTA_ANGLE
