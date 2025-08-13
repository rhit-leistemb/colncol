import pygame
from Game import Game

class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background = 0
        self.background_color = pygame.Color("black")
        self.font = pygame.font.Font(None, 50)

        self.screen_w = self.screen.get_width() // 2
        self.screen_h = self.screen.get_height() // 2

        # State of the game
        self.is_paused = False
        self.is_fin = False
        self.res_present = False

        # Buttons
        self.play_but = self.font.render("START", True, (10, 120, 190))
        # self.restart_but = self.font.render("RESTART", True, (10, 120, 190))
        # self.nxtlvl_but = self.font.render("LEVEL SELECT", True, (10, 120, 190))
        self.exit_but = self.font.render("RESTART AT MENU", True, (10, 120, 190))

        # Image Load ins
        self.title = pygame.image.load("../media/Title.PNG")
        self.pause_image = pygame.image.load("../media/Pause_Button.PNG")
        self.resume_image = pygame.image.load("../media/Resume Button.PNG")
        self.pause_icon = pygame.image.load("../media/Pause Icon.PNG")
        self.game_over_image = pygame.image.load("../media/Game Over.PNG")

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title, (self.screen.get_width() // 2 - self.title.get_width() // 2, 200))
        self.screen.blit(self.play_but, (self.screen_w - self.play_but.get_width() // 2, self.screen_h + 60))
        pygame.display.update()

    def draw_everything(self, background_color):
        self.screen.fill(background_color)
        self.game.draw_game()
        self.screen.blit(self.pause_image, (self.screen.get_width() - self.pause_image.get_width(), 0))
        pygame.display.update()

    def pause(self):
        self.screen.blit(self.resume_image, (self.screen.get_width() - self.resume_image.get_width(), 0))
        self.res_present = True

        slate = pygame.draw.rect(self.screen, (10, 10, 10), (self.screen_w - 225, self.screen_h - 150, 450, 350))

        # self.screen.blit(self.nxtlvl_but, (self.screen_w - self.nxtlvl_but.get_width() // 2, self.screen_h + 60))
        self.screen.blit(self.exit_but, (self.screen_w - self.exit_but.get_width() // 2, self.screen_h + 110))
        self.screen.blit(self.pause_icon, (self.screen_w - (self.pause_icon.get_width() // 2),
                                           self.screen_h - self.pause_icon.get_height()))
        pygame.display.update()

    def draw_end(self):
        self.is_fin = True
        slate = pygame.draw.rect(self.screen, (10, 10, 10), (self.screen_w - 245, self.screen_h - 150,
                                                             self.game_over_image.get_width() + 2, 350))

        #self.screen.blit(self.restart_but, (self.screen_w - self.restart_but.get_width() // 2, self.screen_h + 60))
        #pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_w - (self.restart_but.get_width() // 2) - 5, self.screen_h - 5,
        #                 self.restart_but.get_width() + 10, self.restart_but.get_height() + 10), 1, 1)
        self.screen.blit(self.exit_but, (self.screen_w - self.exit_but.get_width() // 2, self.screen_h + 110))

        self.screen.blit(self.game_over_image, (self.screen_w - (self.game_over_image.get_width() // 2),
                                                self.screen_h - self.game_over_image.get_height() - 20))
        pygame.display.update()




