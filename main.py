import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display (window)
# We'll make it a standard size for now
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AI Evasion Game") # Title of the window

# 3. Game Loop (The heart of any game)
running = True
while running:
    # 4. Event Handling
    # This is where we check for user input (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user clicks the 'X' to close
            running = False # Stop the loop

    # 5. Drawing (We'll add drawing the logo here later)
    # For now, let's just fill the background black
    screen.fill((0, 0, 0)) # RGB for black

    # 6. Update the display
    # This makes everything we've drawn visible
    pygame.display.flip()

# 7. Quit Pygame
pygame.quit()
print("Game Over!")