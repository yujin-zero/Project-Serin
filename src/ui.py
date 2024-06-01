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
        
        image_size=50;
        
        for i in range(5):
            pygame.draw.rect(self.screen, (0,0,0), (x,y,image_size,image_size),2)
            x+=image_size  

        #아이템 그리기
        x=0
       #item_list = self.inventory.item_list
        #for item in item_list:

                
        
        
    
        
        

    
        