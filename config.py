# Game Configuration and Constants

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Game speeds
FPS = 60
PLAYER_SPEED = 5
ENEMY_BASE_SPEED = 4
ROAD_SPEED = 3

# Car dimensions
CAR_WIDTH = 40
CAR_HEIGHT = 60

# Player starting position
PLAYER_START_X = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT - 80

# Enemy spawn settings
ENEMY_SPAWN_RATE = 60  # frames between spawns
MIN_ENEMY_SPAWN_RATE = 30  # minimum spawn rate (increases difficulty)

# Game states
GAME_STATE_LOGIN = "login"
GAME_STATE_MENU = 1
GAME_STATE_PLAYING = 2
GAME_STATE_GAME_OVER = 3

# Difficulty scaling
DIFFICULTY_INCREASE_INTERVAL = 5000  # milliseconds
SPEED_INCREASE_PER_LEVEL = 0.5

# User authentication
MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 50
