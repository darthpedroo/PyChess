import pygame
import time
class Board:
    def __init__(self):
        self.SquareSize = 50
        self.Colors = [[0,0,0],[255,255,255]]
        self.rows = 9 #This is one more number cause the loop ends in one less (9 -> 8)
        self.columns = 9
        self.LeftCorner = [100,100]
    
    def drawSquare(self,surface,col,row):
        
        if row%2 == 0:
            tempColor = self.Colors[col%2 == 0]
        else:
            tempColor = self.Colors[col%2 == 1]
            
        pygame.draw.rect(surface, tempColor, pygame.Rect(self.LeftCorner[0]+(self.SquareSize*col), self.LeftCorner[1]+(self.SquareSize*row), self.SquareSize, self.SquareSize))
        pygame.display.flip()
    
    def drawBoard(self,surface):
        for row in range(1,self.rows):
            for col in range(1,self.columns):
                self.drawSquare(surface, col,row)
                


        
    
    
        

