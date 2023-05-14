from square3 import Square
from const import *

class Snake:
    def __init__(self, color, pos):
        self.color = color
        self.head = Square(pos)
        self.body = [self.head]
        self.turns = {}
    
    def move_snake(self, dx, dy):
        # Add turning point direction to turning points so the rest of the snake body knows to turn at that grid
        self.turns[self.head.pos[:]] = [dx, dy]
        for i, square in enumerate(self.body):
            p = square.pos[:]
            # If we are at a point where snake turned

            if p in self.turns:
                print('meh')
                turn = self.turns[p]
                square.move(turn[0], turn[1])
                # If we reached snake's tail, remove the turning point
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            # If we are not turning the snake
            else:  
                # If the snake reaches the edge of the screen we will make it appear on the opposite side
                if square.dx == -1 and square.pos[0] <= 0:
                    print(square.pos)
                    square.pos = (COLS - 1, square.pos[1])
                elif square.dx == 1 and square.pos[0] >= COLS - 1:
                    square.pos = (0,square.pos[1])
                elif square.dy == 1 and square.pos[1] >= ROWS - 1:
                    square.pos = (square.pos[0], 0)
                elif square.dy == -1 and square.pos[1] <= 0:
                    square.pos = (square.pos[0], ROWS - 1)
                # If we haven't reached the edge just move in our current direction
                else:
                    square.move(square.dx, square.dy)  
    
    def add_square(self):
        tail = self.body[-1]
        dx, dy = tail.dx, tail.dy
        
        # We need to know which side of the snake to add the cube to.
        # So we check what direction we are currently moving in to determine if we
        # need to add the cube to the left, right, above or below.
        if dx == 1 and dy == 0:
            self.body.append(Square((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Square((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Square((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Square((tail.pos[0], tail.pos[1] + 1)))
        
        # We then set the cubes direction to the direction of the snake.
        self.body[-1].dx = dx
        self.body[-1].dy = dy


    def draw(self, screen):
        for i, square in enumerate(self.body):
            if i == 0:
                square.draw(screen, eyes=True)
            else:
                square.draw(screen)

    def reset(self, pos):
        self.head = Square(pos)
        self.body = [self.head]
        self.turns = {}