import pygame

class Board:
    def __init__(self):
        self.SquareSize = 60
        self.Colors = [[0,0,0],[255,255,255]]
        self.rows = 8
        self.columns = 8
    
    def drawSquare(self,surface):
        pygame.draw.rect(surface, self.Colors[1], pygame.Rect(0, 0, self.SquareSize, self.SquareSize))
        pygame.display.flip()
    
    
        

