import Serin
import pygame

class Ui:
    def __init__(self,  inventory, screen):
        self.inventory = inventory
        self.screen = screen

    def draw(self):
        self.draw_inventory()

        

    def draw_inventory(self):
        x = 0;
        y = 50;
        
        for i in range(5):
            pygame.draw.rect(self.screen, (0,0,0), (x,y,50,50))
            x+=50  

        
        
    
        
        

    
        