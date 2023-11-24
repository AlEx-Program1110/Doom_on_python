# variables init
import math
import pygame

pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

HALF_HEIGHT = HEIGHT // 2
HALF_WIDTH = WIDTH // 2

player_pos = [600, 400]
player_angle = 0
player_speed = 2

FPS = 300

BLOCK_CHAR = 'B'
TITLE = 60

FOV = math.pi / 3
PLAYER_FOV = FOV / 2
NUMBER_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUMBER_RAYS
DIST = NUMBER_RAYS / (2 * math.tan(PLAYER_FOV))
COOFIC = 3 * DIST * TITLE
SCALE = WIDTH // NUMBER_RAYS

# colors
BLACK = (0, 0, 0)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
