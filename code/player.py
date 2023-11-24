import math

import pygame


class Player:
    def __init__(self, pos, angle, speed):
        self.pos = [600, 400]
        self.angle = 0
        self.speed = 2

    def move(self):
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos[0] += self.speed * cos_angle
            self.pos[1] += self.speed * sin_angle
        if keys[pygame.K_s]:
            self.pos[0] -= self.speed * cos_angle
            self.pos[1] -= self.speed * sin_angle
        if keys[pygame.K_a]:
            self.pos[0] += self.speed * cos_angle
            self.pos[1] -= self.speed * sin_angle
        if keys[pygame.K_d]:
            self.pos[0] -= self.speed * cos_angle
            self.pos[1] += self.speed * sin_angle

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    # get

    def get_speed(self):
        return self.speed

    def get_angle(self):
        return self.angle

    def get_pos_x(self):
        return self.pos[0]

    def get_pos_y(self):
        return self.pos[1]

    def get_pos(self):
        return self.pos

    # set

    def set_speed(self, speed):
        self.speed = speed

    def set_angle(self, angle):
        self.angle = angle

    def set_pos_x(self, x):
        self.pos[0] = x

    def set_pos_y(self, y):
        self.pos[1] = y

    def set_pos(self, pos):
        self.pos = pos
