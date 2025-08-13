import random
import pygame
from Pillar import Pillar
import sys

class Blip:
    def __init__(self, screen: pygame.Surface, color, x, y, radius, width, speed, lives, horz, vert):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.rad = radius
        self.width = width
        self.lives = lives

        self.horz = horz
        self.vert = vert

        self.x_speed = speed
        self.y_speed = speed
        self.ogx_speed = speed
        self.ogy_speed = speed
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])

        self.hit_box = pygame.Rect(self.x, self.y, self.rad, self.rad)
        self.background_color = pygame.Color("black")

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad, self.width)

    def move(self):
        self.x += self.x_speed * self.x_direction
        self.y += self.y_speed * self.y_direction

    def crushed_by(self, pillar_hb):
        return self.hit_box.colliderect(pillar_hb)

    def is_destroyed(self):
        del self

