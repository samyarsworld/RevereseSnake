import pygame
from square import Square
from const import *

class Snake:
    def __init__(self, color, head_pos):
        self.color = color
        self.head = Square(color, head_pos)
        self.body = [self.head]
        self.turns = {}

    def move(self, dx, dy):
        # Add the position of the turn to turns
        self.turns[self.head.pos] = [dx, dy]

        # Move all body squares
        for i, sq in enumerate(self.body):
            p = sq.pos
            if p in self.turns:
                sq.move(self.turns[p])
                # If last body part is on the turn, remove the turning point
                if len(self.body) - 1 == i: 
                    self.turns.pop(p)
            else:
                # If is going out of bounds, appear on theother side
                if sq.dx == -1 and sq.pos[0] <= START_X: sq.pos = (END_X, sq.pos[1])
                elif sq.dx == 1 and sq.pos[0] >= END_X: sq.pos = (START_X, sq.pos[1])
                elif sq.dy == 1 and sq.pos[1] >= END_X: sq.pos = (sq.pos[0], START_Y)
                elif sq.dy == -1 and sq.pos[1] <= START_Y: sq.pos = (sq.pos[0], END_Y)
                # Else move in the specified direction
                else: sq.move((sq.dx, sq.dy))
                
    def draw(self, screen):
        for i, sq in enumerate(self.body):
            if i == 0:
                sq.draw(screen, isHead=True)
            else:
                sq.draw(screen)
    
    def add_body(self):
        tail = self.body[-1]
        tail_dx, tail_dy = tail.pos[0], tail.pos[1]
        pos = (tail.pos[0] - tail_dx * SQ_SIZE, tail.pos[1] - tail_dy * SQ_SIZE)

        self.body.append(Square(self.color, pos, tail_dx, tail_dy))


