import pygame
pygame.font.init()
pygame.mixer.init()

# Dimensions
WIN_WIDTH = 1200
WIN_HEIGHT = 600
SQ_SIZE = 20

GAME_OFFSET = 3 * SQ_SIZE

GAME_WIDTH = WIN_WIDTH - 2 * GAME_OFFSET 
GAME_HEIGHT = WIN_HEIGHT - 3 * GAME_OFFSET 
START_X = GAME_OFFSET
END_X = GAME_WIDTH
START_Y = GAME_OFFSET
END_Y = GAME_HEIGHT

ROWS = GAME_HEIGHT // SQ_SIZE
COLS = GAME_WIDTH // SQ_SIZE

# Positions
GAME_SCREEN_POS = (GAME_OFFSET, GAME_OFFSET, GAME_WIDTH, GAME_HEIGHT)
RIBBON_POS = (GAME_OFFSET - SQ_SIZE, GAME_OFFSET - SQ_SIZE, GAME_WIDTH + 2 * SQ_SIZE, GAME_HEIGHT + 2 * SQ_SIZE)

# Colors
WIN_BG_COLOR = (0, 0, 0)
GAME_BG_COLOR = (21, 0, 41) # Deep purple
RIBBON_COLOR = (120, 120, 120) # Grey

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARK_PURPLE = (0, 94, 6)
LIGHT_PURPLE = (37,117, 42)

# Screen texts
WIN_FONT = pygame.font.SysFont('comicsans', 100)
LOSE_FONT = pygame.font.SysFont('comicsans', 100)

# Sounds
# EAT_SOUND = pygame.mixer.Sound('assets/sounds/.mp3')
# LOSE_SOUND = pygame.mixer.Sound('assets/sounds/.mp3')

# Screen update per second
FPS = 60

# SNAKE_INIT = (2 * SQ_SIZE + WIDTH * 5 // SQ_SIZE, HEIGHT * 10 // SQ_SIZE, SQ_SIZE, SQ_SIZE)