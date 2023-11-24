import pygame
from setting_variables import *
from player import Player
from map import map, TITLE
import math


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
        draw(window, player, clock)

        pygame.display.flip()
        clock.tick(FPS)


def moves(player):
    player.move()


def draw(window, player, clock):
    pygame.draw.rect(window, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(window, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    ray_casting(window, player.get_pos(), player.get_angle())

    fps_now = pygame.font.SysFont('Arial', 36, bold=True)
    render = fps_now.render(str(int(clock.get_fps())), 0, BLACK)
    window.blit(render, (WIDTH - 56, 10))


def ray_casting(window, player_pos, player_angle):
    cur_angle = player_angle - PLAYER_FOV
    xo, yo = player_pos
    xp, yp = (xo // TITLE) * TITLE, (yo // TITLE) * TITLE
    for ray in range(NUMBER_RAYS + 20):
        sin_angle = math.sin(cur_angle)
        cos_angle = math.cos(cur_angle)
        depth_vertical = 1
        depth_h = 1
        if cos_angle >= 0:
            x = xp + TITLE
            dx = 1
        else:
            x = xp
            dx = -1
        for i in range(0, WIDTH, TITLE):
            depth_vertical = (x - xo) / cos_angle
            y = yo + depth_vertical * sin_angle
            if (((x + dx) // TITLE) * TITLE, (y // TITLE) * TITLE) in map:
                break
            x += dx * TITLE
        if sin_angle >= 0:
            y = yp + TITLE
            dy = 1
        else:
            y = yp
            dy = -1
        for i in range(0, HEIGHT, TITLE):
            depth_h = (y - yo) / sin_angle
            x = xo + depth_h * cos_angle
            if ((x // TITLE) * TITLE, ((y + dy) // TITLE) * TITLE) in map:
                break
            y += dy * TITLE
        depth = depth_vertical
        if depth > depth_h:
            depth = depth_h
        depth *= math.cos(player_angle - cur_angle)
        height = min(int(COOFIC / depth), 2 * HEIGHT)
        c = 255 / (1 + depth * depth * 0.0002)
        color = (c, c // 2, c // 3)
        pygame.draw.rect(window, color, (ray * SCALE, HALF_HEIGHT - height // 2, SCALE, height))
        cur_angle += DELTA_ANGLE
