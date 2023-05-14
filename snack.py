import pygame
from const import *
import random

class Snack:
    def __init__(self, color=GREEN):
        self.color = color
        self.snack_pos = (random.randrange(GAME_OFFSET, GAME_WIDTH, SQ_SIZE), random.randrange(GAME_OFFSET, GAME_HEIGHT, SQ_SIZE))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.snack_pos[0], self.snack_pos[1], SQ_SIZE, SQ_SIZE))