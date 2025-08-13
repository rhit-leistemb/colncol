import pygame
import random
import time
from Pillar import Pillar
from Blip import Blip
from Score import Scoreboard

class Game:
    def __init__(self, screen: pygame.Surface, score, life_count, b_color, blip_x, blip_y, b_radius, b_width, b_speed, b_lives, background, level, ready):
        self.screen = screen
        self.b_color = b_color
        self.blip_x = blip_x
        self.blip_y = blip_y
        self.b_rad = b_radius
        self.b_width = b_width
        self.b_speed = b_speed
        self.background = background

        self.temp = b_lives
        self.b_lives = self.temp
        self.scoreboard = score

        self.pillar_horz = Pillar(screen, 'along bottom', 375, 700, None)
        self.pillar_vert = Pillar(screen, 'along side', 0, 375, self.pillar_horz)
        self.pillar_horz.other_pillar = self.pillar_vert
        self.blip = Blip(self.screen, self.b_color, self.blip_x, self.blip_y, self.b_rad, self.b_width, self.b_speed, self.b_lives,
                         self.pillar_horz, self.pillar_vert)

        self.life_count = life_count
        self.life_count.lives = b_lives
        pygame.display.update()

        self.bounce_timex = 1
        self.bounce_timey = 1
        self.impact_time = 1

        self.level = level

        self.ready_to_go = ready

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.blip.draw()
        self.pillar_horz.draw()
        self.pillar_vert.draw()
        self.scoreboard.draw()
        self.life_count.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        self.blip.move()
        self.pillar_horz.move()
        self.pillar_vert.move()

        r = self.b_color[0] - self.background
        g = self.b_color[1] + 20
        b = self.b_color[2] + 20
        blended_backcolor = (r, g, b)

        # Blip bounces off wall
        if (time.time() - self.bounce_timex) > 0.1:
            if self.blip.x >= (self.screen.get_width() - self.blip.rad) or self.blip.x <= (0 + self.blip.rad):
                self.blip.x_direction = self.blip.x_direction * (-1)
                self.blip.x_speed = random.randint(self.blip.ogx_speed - 2, self.blip.ogx_speed + 2)
                self.bounce_timex = time.time()
                if self.background != -69:
                    self.blip.background_color = pygame.Color(blended_backcolor)
        if (time.time() - self.bounce_timey) > 0.1:
            if self.blip.y >= (self.screen.get_height() - self.blip.rad) or self.blip.y <= (0 + self.blip.rad + 20):
                self.blip.y_direction = self.blip.y_direction * (-1)
                self.blip.y_speed = random.randint(self.blip.ogy_speed - 2, self.blip.ogy_speed + 2)
                self.bounce_timey = time.time()
                if self.background != -69:
                    self.blip.background_color = pygame.Color((0, 0, 0))

        # Blip crushed by Pillar
        if (time.time() - self.impact_time) > 0.3:
            if self.blip.crushed_by(self.pillar_horz.pillar_hitbox) or self.blip.crushed_by(self.pillar_horz.other_pillar_hitbox):
                print("blip got hit")
                self.blip.lives -= 1
                self.life_count.lives -= 1
                self.impact_time = time.time()
                if self.blip.lives == 0:
                    self.scoreboard.score += 10
                    self.blip.lives = self.temp
                    self.blip.is_destroyed()
                    self.level += 1
            pygame.display.update()

    def cheat(self):
        if (time.time() - self.impact_time) > 0.3:
            self.blip.lives -= 1
            self.life_count.lives -= 1
            self.impact_time = time.time()
            if self.blip.lives == 0:
                self.scoreboard.score += 10
                self.blip.lives = self.temp
                self.blip.is_destroyed()
                self.level += 1
        pygame.display.update()

    def is_ready(self):
        self.ready_to_go = 1



