import pygame
import time


class Pillar:
    def __init__(self, screen, orientation, x, y, other_pillar):
        self.screen = screen
        self.orientation = orientation
        self.x = x
        self.y = y
        self.extension = 50
        self.retract_by = 0
        self.rect = 0
        self.other_rect = 0
        self.other_pillar = other_pillar

        # Added these two following lines
        self.pillar_hitbox = 0
        self.other_pillar_hitbox = 0

    def draw(self):
        if self.orientation == 'along bottom':
            self.rect = pygame.draw.rect(self.screen, pygame.Color('white'), (self.x, self.y, 150, self.extension), 1, 1)
            self.other_rect = pygame.draw.rect(self.screen, pygame.Color('white'), (self.other_pillar.x, self.other_pillar.y, self.other_pillar.extension, 150), 1, 1)
        if self.orientation == 'along side':
            self.rect = pygame.draw.rect(self.screen, pygame.Color('white'), (self.x, self.y, self.extension, 150), 1, 1)
            self.other_rect = pygame.draw.rect(self.screen, pygame.Color('white'), (self.other_pillar.x, self.other_pillar.y, 150, self.other_pillar.extension), 1, 1)
        # Also added these two following lines
        self.pillar_hitbox = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.other_pillar_hitbox = pygame.Rect(self.other_rect.x, self.other_rect.y, self.other_rect.width,
                                               self.other_rect.height)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.orientation == 'along bottom':
            if pressed_keys[pygame.K_LEFT]:
                self.x = self.x - 5
                if self.x < 0:
                    self.x = self.x + 5
            if pressed_keys[pygame.K_RIGHT]:
                self.x = self.x + 5
                if self.x > self.screen.get_width()-self.rect.width:
                    self.x = self.x - 5
        if self.orientation == 'along side':
            if pressed_keys[pygame.K_q]:
                self.y = self.y - 5
                if self.y < 0:
                    self.y = self.y + 5
            if pressed_keys[pygame.K_a]:
                self.y = self.y + 5
                if self.y > self.screen.get_height()-self.rect.height:
                    self.y = self.y - 5

    def extend(self):
        # print(self.retract_by)
        print(self.other_pillar_hitbox)
        if self.orientation == 'along bottom':
            for k in range(500):
                if self.pillar_collide() is True:
                    print('bottompillar has hit!')
                    break
                else:
                    self.extension = self.extension + 1
                    self.retract_by = self.retract_by + 1
                    self.y = self.y - 1
        if self.orientation == 'along side':
            for k in range(500):
                if self.pillar_collide() is True:
                    print('sidepillar has hit!')
                    break
                else:
                    self.extension = self.extension + 1
                    self.retract_by = self.retract_by + 1

    def retract(self):
        for k in range(self.retract_by):
            if self.orientation == 'along bottom':
                self.extension = self.extension - 1
                self.y = self.y + 1
            if self.orientation == 'along side':
                self.extension = self.extension - 1
        self.retract_by = 0

    def pillar_collide(self):
        self.pillar_hitbox = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.other_pillar_hitbox = pygame.Rect(self.other_rect.x, self.other_rect.y, self.other_rect.width, self.other_rect.height)
        return self.pillar_hitbox.colliderect(self.other_pillar_hitbox)

        # Your original code for the function below
        # pillar_hitbox = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        # other_pillar_hitbox = pygame.Rect(self.other_rect.x, self.other_rect.y, self.other_rect.width,
        #                                        self.other_rect.height)
        # return pillar_hitbox.colliderect(other_pillar_hitbox)





