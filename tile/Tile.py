import pygame
from colorsF.Colors import Colors
class Tile:
    def __init__(self) -> None:
        self.TileSize = 50
        self.SetOfColors = 2

    def drawTile(self, surface,col,row, LeftCorner):
        if row%2 == 0:
            SquareColor = Colors().get_ColorPallete(self.SetOfColors,col%2 == 0)
        else:
            SquareColor = Colors().get_ColorPallete(self.SetOfColors,col%2 == 1)
        pygame.draw.rect(surface, SquareColor, pygame.Rect(LeftCorner[0]+(self.TileSize*(col-1)), LeftCorner[1]+(self.TileSize*(row-1)), self.TileSize, self.TileSize)) #Col and row are substracted by 1 so as the board starts in the proper place and not moved by one (basically to make col and row = 0 and not 1)
        pygame.display.flip()