import random
import pygame
from const import *

class Snack:
    def __init__(self, color, pos):
        self.color = color
        self.pos= pos
    
    def random_snack(self, body):
        # Keep generating random positions until we get a valid one
        while True:  
            x = random.randrange(COLS)
            y = random.randrange(ROWS)
            # Get all the posisitons of cubes in our snake to avoid dropping snack on the snake
            if len(list(filter(lambda z: z.pos == (x, y), body))) > 0:
                continue
            else:
                break
        self.pos = (x, y)

    def draw(self, screen):
        i = self.pos[0] # Current row
        j = self.pos[1] # Current Column
        pygame.draw.rect(screen, self.color, (i * SQ_SIZE + 1, j * SQ_SIZE + 1, SQ_SIZE - 2, SQ_SIZE - 2))
