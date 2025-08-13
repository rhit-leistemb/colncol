import time

import pygame
import sys
from Game import Game
from View import View

class Controller:
    def __init__(self, game: Game, view: View, game0):
        self.game = game
        self.game0 = game0
        self.view = view

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.pillar_horz.extend()
                if event.key == pygame.K_TAB:
                    self.game.pillar_vert.extend()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.game.pillar_horz.retract()
                if event.key == pygame.K_TAB:
                    self.game.pillar_vert.retract()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                # Temp Cheat Button to iterate through levels, will factor into score
                cheat_hb = pygame.Rect(0, 0, 30, 30)
                if cheat_hb.collidepoint(click_x, click_y):
                    self.game.cheat()

                # Main Menu Button
                play_hb = pygame.Rect((self.view.screen_w - (self.view.play_but.get_width() // 2) - 4, self.view.screen_h + 60 - 4,
                                       self.view.play_but.get_width() + 8, self.view.play_but.get_height() + 8))
                if play_hb.collidepoint(click_x, click_y):
                    self.game.is_ready()

                # Corner Pause Button
                pause_hb = pygame.Rect(self.view.screen.get_width() - self.view.pause_image.get_width(), 0,
                                       self.view.pause_image.get_width(), self.view.pause_image.get_height())
                if pause_hb.collidepoint(click_x, click_y) and self.view.is_paused is False:
                    self.view.is_paused = True

                if pause_hb.collidepoint(click_x, click_y) and self.view.res_present is True:
                    self.view.is_paused = False
                    self.view.res_present = False

                # Interior Menu Buttons
                if self.view.is_paused is True or self.view.is_fin is True:
                    # restart_hb = pygame.Rect(self.view.screen_w - (self.view.restart_but.get_width() // 2) - 4, self.view.screen_h + 60 - 4,
                    #                      self.view.restart_but.get_width() + 8, self.view.restart_but.get_height() + 8)
                    # if restart_hb.collidepoint(click_x, click_y) and self.view.is_fin is True:
                    #     print("should restart game but may cut")  # go back ot lvl 1? or maybe go to prev lvl

                    # nxtlvl_hb = pygame.Rect(self.view.screen_w - (self.view.nxtlvl_but.get_width() // 2) - 4, self.view.screen_h + 60 - 4,
                    #                      self.view.nxtlvl_but.get_width() + 8, self.view.nxtlvl_but.get_height() + 8)
                    # if nxtlvl_hb.collidepoint(click_x, click_y) and self.view.is_paused is True:
                    #     print("Go to the next level! HAve i implemented that yet?")

                    exit_hb = pygame.Rect(self.view.screen_w - (self.view.exit_but.get_width() // 2) - 4, self.view.screen_h + 110 - 4,
                                        self.view.exit_but.get_width() + 8, self.view.exit_but.get_height() + 8)
                    if exit_hb.collidepoint(click_x, click_y):
                        self.game0.ready_to_go = 0
                        print("getting clicked")

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
