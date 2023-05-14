import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from const import *
from snake3 import Snake
from snack3 import Snack
from square3 import Square


class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake')
        self.snake = Snake((255, 0, 0), (10, 10))
        self.snack = Snack((0, 255, 0), (5, 5))
        self.flag = True
        self.clock = pygame.time.Clock()
    
    def create_background(self):
        # Background color
        self.screen.fill((0, 0, 0))
        # Create grids
        x = y = 0
        for _ in range(ROWS):
            x, y = x + SQ_SIZE, y + SQ_SIZE
            pygame.draw.line(self.screen, (255, 255, 255), (x, 0), (x, WIDTH))
            pygame.draw.line(self.screen, (255, 255, 255), (0, y), (WIDTH, y))


    def message_box(self, subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

    def mainloop(self):
        while self.flag:
            # Delay for better user experience
            # pygame.time.delay(10)
            self.clock.tick(60)
            
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.snake.move_snake(-1, 0)
                elif keys[pygame.K_RIGHT]:
                    self.snake.move_snake(1, 0)
                elif keys[pygame.K_UP]:
                    self.snake.move_snake(0, -1)
                elif keys[pygame.K_DOWN]:
                    self.snake.move_snake(0, 1)

                if self.snake.body[0].pos == self.snack.pos:
                    self.snake.add_square()
                    self.snack.random_snack(self.snake.body)


                for x in range(len(self.snake.body)):
                    # This will check if any of the positions in our body list overlap
                    if self.snake.body[x].pos in list(map(lambda z: z.pos, self.snake.body[x + 1:])): 
                        print('Score: ', len(self.snake.body))
                        self.message_box('You Lost!', 'Play again...')
                        self.snake.reset((10, 10))
                        break
                # Create background
                self.create_background()
                self.snake.draw(self.screen)
                self.snack.draw(self.screen)

                # Update screen
                pygame.display.update()

    

main = Main()
main.mainloop()
