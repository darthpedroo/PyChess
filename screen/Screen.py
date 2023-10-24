import pygame
from board.Board import Board

class Screen:

    def __init__(self):
        self.Width = 600
        self.Height = 800
        self.Title = "PyChess"

    def drawScreen(self):
        surface = pygame.display.set_mode((self.Width, self.Height)) 
        pygame.display.set_caption(self.Title)
        Board().drawSquare(surface)
    
    def updateScreen(self):
        pygame.display.update()

