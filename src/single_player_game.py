import os

from button import Button
from closed_window_exception import ClosedWindowException
from dots_and_boxes import DotsAndBoxes

import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class SinglePlayerGame:
    def __init__(self, screen:pygame.surface.Surface, horizontal_squares:int, vertical_squares:int, player_turn:str):
        self.screen = screen
        self.board_size = (horizontal_squares, vertical_squares)
        self.game = DotsAndBoxes(vertical_squares, horizontal_squares)
        self.background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('..', 'assets', 'old-paper-with-pencil-on-wooden-table-free-photo.jpg')), (800, 600))
        
        self.score_font = pygame.font.Font(None, 30)
        self.white_area = Button(360, 433, 121, 70, 'white_pixel.png', 'white_pixel.png', pygame.Surface((0, 0)))
        self.white_area2 = Button(150, 190, 520, 70, 'white_pixel.png', 'white_pixel.png', pygame.Surface((0, 0)))
        self.player1 = Button(80, 50, 530, 90, 'green_pixel.png', 'green_pixel.png', self.score_font.render('Player1:', True, BLUE))
        self.player2 = Button(80, 50, 530, 190, 'green_pixel.png', 'green_pixel.png', self.score_font.render('Player2:', True, RED))
        self.player1_score = Button(40, 50, 615, 90, 'green_pixel.png', 'green_pixel.png', self.score_font.render('0', True, BLUE))
        self.player2_score = Button(40, 50, 615, 190, 'green_pixel.png', 'green_pixel.png', self.score_font.render('0', True, RED))
        self.player_turn = player_turn

        n = self.board_size[0]
        m = self.board_size[1]
        self.dots_coordinates = [(int(151 + (i % (m + 1)) * (300 / m)), int(100 + (i // (n + 1)) * (370 / n)))
                                   for i in range((n + 1) * (m + 1))]

        self.edges = []
        for i in range(n * (m + 1) + m * (n + 1)):
            if self.game.is_edge_horizontal(i):
                self.edges.append(Button(self.dots_coordinates[1][0] - self.dots_coordinates[0][0], 4, self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1))][0],self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1))][1], 'black_horizontal_dash_line.png', 'green_pixel.png', pygame.Surface((0, 0))))
            else:
                self.edges.append(Button(4, self.dots_coordinates[n + 1][1] - self.dots_coordinates[0][1], self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1)) - m][0], self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1)) - m][1], 'black_vertical_dash_line.png', 'green_pixel.png', pygame.Surface((0, 0))))
        
        self.clock = pygame.time.Clock()
        back_button_font = pygame.font.Font(None, 30)
        self.back_to_menu = Button(160, 50, 520, 450,'button.png', 'clicked_button.png', back_button_font.render('back to menu', True, (0, 0, 0)))
        self.score = [0, 0]



    def play(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise ClosedWindowException('Closed window')
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = pygame.mouse.get_pos()
                    if self.back_to_menu.is_hovered(click_position):
                        self.back_to_menu.click()
                        playing = False
                    
                    for i in range(len(self.edges)):
                        if self.edges[i].is_hovered(click_position):
                            self.edges[i].click()
                            next_turn = self.game.make_move(i)

                            n = self.board_size[0]
                            m = self.board_size[1]
                            if self.game.is_edge_horizontal(i):
                                horizontal_line = 'red_horizontal_continuos_line.png' if self.player_turn == 'second' else 'blue_horizontal_continuos_line.png'
                                self.edges[i] = Button(self.dots_coordinates[1][0] - self.dots_coordinates[0][0], 4, self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1))][0], self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1))][1], 'green_pixel.png', horizontal_line, pygame.Surface((0, 0))) 
                            else:
                                vertical_line = 'red_vertical_continuos_line.png' if self.player_turn == 'second' else 'blue_vertical_continuos_line.png'
                                self.edges[i] = Button(4, self.dots_coordinates[n + 1][1] - self.dots_coordinates[0][1], self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1)) - m][0], self.dots_coordinates[(i // (2 * m + 1)) * (m + 1) + (i % (2 * m + 1)) - m][1], 'green_pixel.png', vertical_line, pygame.Surface((0, 0)))
                            
                            self.edges[i].click()
                            current_score = self.game.get_score()
                            if current_score != self.score:
                                self.score = current_score
                                self.player1_score = Button(40, 50, 615, 90, 'green_pixel.png', 'green_pixel.png', self.score_font.render(str(current_score[0]), True, BLUE))
                                self.player2_score = Button(40, 50, 615, 190, 'green_pixel.png', 'green_pixel.png', self.score_font.render(str(current_score[1]), True, RED))


            self.screen.blit(self.background_image, (0, 0))
            self.white_area.display(self.screen)
            self.white_area2.display(self.screen)
            self.player1.display(self.screen)
            self.player2.display(self.screen)
            self.back_to_menu.display(self.screen)
            self.player1_score.display(self.screen)
            self.player2_score.display(self.screen)

            for edge in self.edges:
                edge.display(self.screen)

            for dot_coordinates in self.dots_coordinates:
                pygame.draw.circle(self.screen, BLACK, dot_coordinates, 8)
                
            pygame.display.update()
            self.clock.tick(60)
        