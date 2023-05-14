import pygame
from const import *

class Square:
    def __init__(self, pos, dx=1, dy=0, color=(255, 0, 0)):
        self.pos = pos
        self.dx = dx
        self.dy = dy
        self.color = color
    
    def move(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy) 

    def draw(self, screen, eyes=False):
        i = self.pos[0] # Current row
        j = self.pos[1] # Current Column

        pygame.draw.rect(screen, self.color, (i * SQ_SIZE + 1,j * SQ_SIZE + 1, SQ_SIZE - 2, SQ_SIZE - 2))
        # By multiplying the row and column value of our cube by the width and height of each cube we can determine where to draw it
        
        if eyes: # Draws the eyes
            centre = SQ_SIZE // 2
            radius = 3
            circleMiddle = (i * SQ_SIZE + centre - radius, j *SQ_SIZE + 8)
            circleMiddle2 = (i * SQ_SIZE + SQ_SIZE -radius*2, j*SQ_SIZE + 8)
            pygame.draw.circle(screen, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(screen, (0,0,0), circleMiddle2, radius)   