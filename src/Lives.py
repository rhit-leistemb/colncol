import pygame


class Lives(object):
    def __init__(self, screen):
        self.screen = screen
        self.lives = 3
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        lives_string = "Lives: {}".format(self.lives)
        life_count_image = self.font.render(lives_string, True, (255, 255, 255))
        self.screen.blit(life_count_image, (self.screen.get_width() // 2 - 20, 5))