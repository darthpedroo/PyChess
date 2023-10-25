import pygame
from tile.Tile import Tile
class Board:
    def __init__(self):
        self.rows = 9 #This is one more number cause the loop ends in one less (9 -> 8)
        self.columns = 9
        self.LeftCorner = [100,200]
    
    def drawBoard(self,surface):
        for row in range(1,self.rows):
            for col in range(1,self.columns):
                Tile().drawTile(surface,col,row,self.LeftCorner)


