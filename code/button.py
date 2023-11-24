import pygame
from setting_variables import *


class Button_menu:
    def __init__(self, text, width, height):
        self.text = text
        self.width = width
        self.height = height

    def draw(self, x, y, window):
        pygame.draw.rect(window, RED, (x, y, x + self.width, y + self.height))

    def move_mouse_button(self, x, y):
        return (x < pygame.mouse.get_pos()[0] < x + self.width) and (
                y < pygame.mouse.get_pos()[1] < y + self.height) and \
            pygame.mouse.get_pressed()[0]
