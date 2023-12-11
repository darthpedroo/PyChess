import pygame 
from screen.Screen import Screen

pygame.init() 

screen = Screen()
screen.drawScreen()

exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    screen.updateScreen() 
