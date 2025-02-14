import time
import os

from button import Button
from closed_window_exception import ClosedWindowException

import pygame

class Menu:
    def __init__(self, screen:pygame.surface.Surface):
        self.screen = screen
        self.background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('..', 'assets', 'old-paper-with-pencil-on-wooden-table-free-photo.jpg')), (800, 600))

    def main_menu(self) -> str:
        text_font = pygame.font.Font(None, 70)
        button_font = pygame.font.Font(None, 30)
        
        # I use green_pixel.png as a transparent background for the text
        text = Button(300, 160, 250, 50, 'green_pixel.png', 'green_pixel.png', text_font.render('Dots&Boxes', True, (0, 0, 0)))
        single_player = Button(160, 80, 320, 200, 'button.png', 'clicked_button.png', button_font.render('SinglePlayer', True, (0, 0, 0)))
        multiplayer = Button(160, 80, 320, 320, 'button.png', 'clicked_button.png', button_font.render('MultiPlayer', True, (0, 0, 0)))

        game_type = None
        while game_type is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise ClosedWindowException('Closed window')
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = pygame.mouse.get_pos()
                    if single_player.is_hovered(click_position):
                        single_player.click()
                        game_type = 'single_player'
                    if multiplayer.is_hovered(click_position):
                        multiplayer.click()
                        game_type = 'multiplayer'
            
            self.screen.blit(self.background_image, (0, 0))
            text.display(self.screen)
            single_player.display(self.screen)
            multiplayer.display(self.screen)
            pygame.display.update()
        
        time.sleep(0.1)
        return game_type
    
    def game_size(self) -> str:
        text_font = pygame.font.Font(None, 70)
        button_font = pygame.font.Font(None, 50)
        back_button_font = pygame.font.Font(None, 30)

        text = Button(300, 160, 250, 50, 'green_pixel.png', 'green_pixel.png', text_font.render('Choose board size', True, (0, 0, 0)))
        three_by_three = Button(100, 60, 240, 260, 'button.png', 'clicked_button.png', button_font.render('3x3', True, (0, 0, 0)))
        four_by_four = Button(100, 60, 440, 260, 'button.png', 'clicked_button.png', button_font.render('4x4', True, (0, 0, 0)))
        back_to_menu = Button(160, 50, 520, 450,'button.png', 'clicked_button.png', back_button_font.render('back to menu', True, (0, 0, 0)))

        board_size = None
        while board_size is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise ClosedWindowException('Closed window')
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = pygame.mouse.get_pos()
                    if three_by_three.is_hovered(click_position):
                        three_by_three.click()
                        board_size = '3x3'
                    if four_by_four.is_hovered(click_position):
                        four_by_four.click()
                        board_size = '4x4'
                    if back_to_menu.is_hovered(click_position):
                        back_to_menu.click()
                        board_size = 'back_to_menu'

            self.screen.blit(self.background_image, (0, 0))
            text.display(self.screen)
            three_by_three.display(self.screen)
            four_by_four.display(self.screen)
            back_to_menu.display(self.screen)
            pygame.display.update()
        
        time.sleep(0.1)
        return board_size
    
    def first_or_second(self) -> str:
        text_font = pygame.font.Font(None, 70)
        button_font = pygame.font.Font(None, 35)
        back_button_font = pygame.font.Font(None, 30)

        text = Button(300, 160, 250, 50, 'green_pixel.png', 'green_pixel.png', text_font.render('Which turn is yours?', True, (0, 0, 0)))
        first = Button(100, 60, 240, 260, 'button.png', 'clicked_button.png', button_font.render('First', True, (0, 0, 0)))
        second = Button(100, 60, 440, 260, 'button.png', 'clicked_button.png', button_font.render('Second', True, (0, 0, 0)))
        back_to_menu = Button(160, 50, 520, 450,'button.png', 'clicked_button.png', back_button_font.render('back to menu', True, (0, 0, 0)))

        first_or_second = None
        while first_or_second is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise ClosedWindowException('Closed window')
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = pygame.mouse.get_pos()
                    if first.is_hovered(click_position):
                        first.click()
                        first_or_second = 'first'
                    if second.is_hovered(click_position):
                        second.click()
                        first_or_second = 'second'
                    if back_to_menu.is_hovered(click_position):
                        back_to_menu.click()
                        first_or_second = 'back_to_menu'

            self.screen.blit(self.background_image, (0, 0))
            text.display(self.screen)
            first.display(self.screen)
            second.display(self.screen)
            back_to_menu.display(self.screen)
            pygame.display.update()
        
        time.sleep(0.1)
        return first_or_second

