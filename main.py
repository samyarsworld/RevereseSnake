import sys
import pygame
import random
import tkinter as tk
from tkinter import messagebox

from snake import Snake
from snack import Snack

from const import *


pygame.init()
# enable key repeat with a 500 millisecond delay and 50 millisecond interval
pygame.key.set_repeat(150, 50)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def display_game(snake, snack):
    # Display background
    screen.fill(WIN_BG_COLOR)
    pygame.draw.rect(screen, RIBBON_COLOR, RIBBON_POS)
    pygame.draw.rect(screen, GAME_BG_COLOR, GAME_SCREEN_POS)
    # Grids
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (GAME_OFFSET, row * SQ_SIZE + GAME_OFFSET), (GAME_WIDTH + GAME_OFFSET, row * SQ_SIZE + GAME_OFFSET))
    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * SQ_SIZE + GAME_OFFSET, GAME_OFFSET), (col * SQ_SIZE + GAME_OFFSET, GAME_HEIGHT + GAME_OFFSET))

    # Display snake
    snake.draw(screen)
    # Display snack
    snack.draw(screen)

def main():
    # Render speed
    clock.tick(FPS)
    # Initialize snake head position at a random location
    snake = Snake(RED, (random.randrange(GAME_OFFSET, GAME_WIDTH, SQ_SIZE), random.randrange(GAME_OFFSET, GAME_HEIGHT, SQ_SIZE)))
    # Initialize snack position at a random location
    snack = Snack()

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Moving the snake
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                snake.move(-1, 0)
            elif keys[pygame.K_RIGHT]:
                snake.move(1, 0)
            elif keys[pygame.K_UP]:
                snake.move(0, -1)
            elif keys[pygame.K_DOWN]:
                snake.move(0, 1)
            
            # Check if the snack is eaten
            if snake.body[0].pos == snack.snack_pos:
                snake.add_body()
                snack = Snack()

            # Check if we have hit the snake body
            if snake.body[0].pos in list(map(lambda s: s.pos, snake.body[1:])):
                flag = False
                message_box('You Lost!', 'Play again...')
                break
        
   
        display_game(snake, snack)
        pygame.display.update()

    pygame.time.delay(2000)
    main()
        
if __name__ == '__main__':
    main()

