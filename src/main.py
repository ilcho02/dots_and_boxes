from menu import Menu
from closed_window_exception import ClosedWindowException
from single_player_game import SinglePlayerGame

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_POSITION = (0, 0)

class Game:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("dots&boxes")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        

    def start(self):
        running:bool = True

        menu = Menu(self.screen)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            game_type = None
            board_size = None
            first_or_second = None
            try:
                game_type = menu.main_menu()
            except ClosedWindowException:
                break
            
            if game_type == 'single_player':
                try:
                    board_size = menu.game_size()
                except ClosedWindowException:
                    break

                if board_size == 'back_to_menu':
                    continue
                elif board_size == '3x3':
                    try:
                        first_or_second = menu.first_or_second()
                    except ClosedWindowException:
                        break
                    if first_or_second == 'back_to_menu':
                        continue
                    game = SinglePlayerGame(self.screen, 3, 3, first_or_second)

                else:
                    try:
                        first_or_second = menu.first_or_second()
                    except ClosedWindowException:
                        break
                    if first_or_second == 'back_to_menu':
                        continue
                    game = SinglePlayerGame(self.screen, 4, 4, first_or_second)
            
            else:
                pass

            try:
                game.play()
            except ClosedWindowException:
                break


            pygame.display.flip()
            self.clock.tick(60)

        
        pygame.quit()


Game().start()
