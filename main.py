import pygame

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
VIDEO_GAME_TITLE = "Video Game"

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption(VIDEO_GAME_TITLE)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

def draw_scene():
    # Draw sky
    screen.fill(SKY_BLUE)
    
    # Draw grass
    pygame.draw.rect(screen, GREEN, (0, 400, WINDOW_WIDTH, 200))
    
    # Draw tree
    pygame.draw.rect(screen, BROWN, (100, 300, 40, 100))  # Tree trunk
    pygame.draw.circle(screen, GREEN, (120, 270), 50)  # Tree top
    
    # Draw tree apples
    for pos in [(110, 250), (130, 260), (100, 290), (140, 290)]:
        pygame.draw.circle(screen, RED, pos, 10)

    # Draw house
    pygame.draw.rect(screen, RED, (400, 300, 150, 150))  # House base
    pygame.draw.polygon(screen, BROWN, [(400, 300), (475, 250), (550, 300)])  # Roof
    
    # Draw windows
    pygame.draw.rect(screen, PINK, (420, 320, 40, 40))  # Left window
    pygame.draw.rect(screen, PINK, (490, 320, 40, 40))  # Right window
    
    # Draw door
    pygame.draw.rect(screen, PINK, (460, 380, 30, 70))
    
    # Draw sun
    pygame.draw.circle(screen, YELLOW, (700, 100), 50)
    
    # Draw sun rays
    for pos in [(660, 100), (740, 100), (700, 60), (700, 140), (670, 70), (730, 70), (670, 130), (730, 130)]:
        pygame.draw.line(screen, YELLOW, (700, 100), pos, 4)
    
    # Draw cloud
    pygame.draw.circle(screen, WHITE, (200, 100), 30)
    pygame.draw.circle(screen, WHITE, (240, 100), 40)
    pygame.draw.circle(screen, WHITE, (280, 100), 30)
    
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the scene
        draw_scene()

        # Update the screen
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
