import os

import pygame

GREEN = (0, 255, 0)

class Button:
    def __init__(self, width:int, height:int, x:int, y:int, button:str, clicked_button:str, button_content:pygame.surface.Surface):
        self.size = (width, height)
        self.position = (x, y)
        self.button = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', button)), (width, height))
        self.button.set_colorkey(GREEN)
        self.clicked_button = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', clicked_button)), (width, height))
        self.clicked_button.set_colorkey(GREEN)
        self.rect = self.button.get_rect()
        self.rect.move_ip((x, y))
        self.button_content = button_content
        self.content_rect = self.button_content.get_rect()
        self.is_clicked = False

    def display(self, screen:pygame.surface.Surface):
        """
        the button and its content will be displayed on the screen
        """
        if self.is_clicked:
            screen.blit(self.clicked_button, self.position)
        else:
            screen.blit(self.button, self.position)
        screen.blit(self.button_content, (self.rect.center[0] - self.content_rect.width/2, self.rect.center[1] - self.content_rect.height/2))

    def is_hovered(self, mouse_position:tuple[int, int]):
        """
        returns whether or not the button is hovered and isn't clicked
        """
        return not self.is_clicked and self.rect.collidepoint(mouse_position)

    def click(self):
        """
        changes the surface of the button while the mouse is clicking on it
        """
        self.is_clicked = True

