import pygame
from const import SQ_SIZE

class Square:
    def __init__(self, color, pos, dx=1, dy=0):
        self.color = color
        self.pos = pos
        self.dx = dx
        self.dy = dy

    def move(self, dir):
        self.pos = (self.pos[0] + dir[0] * SQ_SIZE, self.pos[1] + dir[1] * SQ_SIZE)

    def draw(self, screen, isHead=False):
        # Draw the square body
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], SQ_SIZE, SQ_SIZE))
        # Draw the eyes
        if isHead:
            centre = SQ_SIZE // 2
            radius = 3
            eye1 = (self.pos[0] + centre - radius, self.pos[1] + 8)
            eye2 = (self.pos[0] + SQ_SIZE - radius * 2, self.pos[1] + 8)
            pygame.draw.circle(screen, (0,0,0), eye1, radius)
            pygame.draw.circle(screen, (0,0,0), eye2, radius)
        