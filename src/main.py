import pygame
from Game import Game
from Controller import Controller
from View import View
from Score import Scoreboard
from Lives import Lives

pygame.init()

screen = pygame.display.set_mode((900, 750))
scoreboard = Scoreboard(screen)
life_count = Lives(screen)

frame_rate = 60
clock = pygame.time.Clock()

gamez = []
game0 = Game(screen, scoreboard, life_count, (0, 0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0)
gamez.append(game0)
game1 = Game(screen, scoreboard, life_count, (250, 70, 10), 300, 300, 80, 50, 4, 3, -69, 2, 1)
gamez.append(game1)
game2 = Game(screen, scoreboard, life_count, (20, 50, 240), 150, 150, 30, 10, 6, 1, -69, 3, 1)  # the Model
gamez.append(game2)
game3 = Game(screen, scoreboard, life_count, (40, 169, 10), 350, 350, 200, 190, 15, 5, -69, 4, 1)
gamez.append(game3)
game4 = Game(screen, scoreboard, life_count, (70, 5, 250), 50, 50, 10, 10, 3, 1, -69, 5, 1)  # 10 levels is the goal
gamez.append(game4)
game5 = Game(screen, scoreboard, life_count, (250, 10, 10), 473, 374, 60, 50, 4, 3, 10, 6, 1)
gamez.append(game5)
#make seperate class so it can be called upon each time?

viewer = View(screen, game0)
controller = Controller(game0, viewer, game0)


def setup():
    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        viewer.draw_menu()
        scoreboard.score = 0
        life_count.lives = 3
        pygame.display.update()
        if game0.ready_to_go == 1:
            main()


def main():
    selected_lvl = 1
    # selected_lvl = int(input("Level Desired-> "))           # level selection commented out for testing
    for selected_lvl in range(selected_lvl, len(gamez)):
        running = True
        viewer = View(screen, gamez[selected_lvl])  # the View
        controller = Controller(gamez[selected_lvl], viewer, game0)  # the Controller
        if game0.ready_to_go == 0:
            running = False
        life_count.lives = gamez[selected_lvl].b_lives
        while running:
            clock.tick(frame_rate)
            controller.get_and_handle_events()
            if viewer.is_paused:
                viewer.pause()
                if game0.ready_to_go == 0:
                    running = False
            else:
                viewer.draw_everything(gamez[selected_lvl].blip.background_color)
                gamez[selected_lvl].run_one_cycle()
                updated_level = gamez[selected_lvl].level
                if updated_level > selected_lvl + 1:
                    gamez[selected_lvl].level -= 1
                    selected_lvl += 1
                    running = False
    if selected_lvl == len(gamez):
        print("!!!!!!!Beat game!!!!!!!!")
        running = True
        while running:
            clock.tick(frame_rate)
            controller.get_and_handle_events()
            viewer.draw_end()
            if game0.ready_to_go == 0:
                running = False

setup()