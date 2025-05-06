import pygame
from network import Network
import pickle
from settings import WHITE, RED, GREEN, BLUE

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.font.init()

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, WHITE)
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.x + round(self.height/2) - round(text.get_height()/2)))
    
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <+ self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False   
    

def redrawWindow(win, game, p):
    win.fill((128,128,128))
    pass

btns = [Button("Rock", 50, 500, RED),
        Button("Scissors", 250, 500, BLUE),
        Button("Paper", 500, 500, GREEN)]

def main():
    pass