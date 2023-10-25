import pygame
from board.Board import Board

class Screen:

    def __init__(self):
        self.Width = 600
        self.Height = 800
        self.Title = "PyChess"
        self.BackgroundColor = (0,0,255)

    def drawScreen(self):
        surface = pygame.display.set_mode((self.Width, self.Height)) 
        surface.fill(self.BackgroundColor)
        pygame.display.set_caption(self.Title)
        Board().drawBoard(surface)
    
    def updateScreen(self):
        pygame.display.update()

