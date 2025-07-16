import pygame
import random

print("--- Script Started ---")

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display (window)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AI Evasion Game - Bikini Bottom Escape!")

# 3. Game Speed and Clock
FPS = 60
clock = pygame.time.Clock()

# Font for displaying score and game over text
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 74)

# 4. Load the background image
try:
    background_image = pygame.image.load("background.jpeg").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    print("Please make sure 'background.jpeg' is in the same directory as main.py")
    pygame.quit()
    exit()

# 5. Load the image and set up its properties (Spongebob - the "AI")
try:
    original_logo_image = pygame.image.load("logo.png").convert_alpha()
except pygame.error as e:
    print(f"Error loading Spongebob image: {e}")
    print("Please make sure 'logo.png' is in the same directory as main.py")
    pygame.quit()
    exit()

logo_size = 80
logo_image = pygame.transform.scale(original_logo_image, (logo_size, logo_size))
# --- NEW: Set colorkey for Spongebob image (assuming white background) ---

# --- END NEW ---
logo_rect = logo_image.get_rect()
logo_rect.center = (screen_width // 2, screen_height // 2)

# 6. Define Spongebob's movement speed and direction
logo_speed = 4
dx = logo_speed
dy = logo_speed

# 7. Load the player image and set up its properties (Your Fist)
try:
    original_player_image = pygame.image.load("player.jpeg")
except pygame.error as e:
    print(f"Error loading player image: {e}")
    print("Please make sure 'player.jpeg' is in the same directory as main.py")
    pygame.quit()
    exit()

player_size = 50
player_image = pygame.transform.scale(original_player_image, (player_size, player_size))
# --- NEW: Set colorkey for Player image (assuming white background) ---
player_image.set_colorkey((255, 255, 255)) # RGB for white
# --- END NEW ---
player_rect = player_image.get_rect()

player_speed = 7

player_rect.centerx = screen_width // 2
player_rect.bottom = screen_height - 10

# 8. Game State Variable
game_over = False

# 9. Coin Properties
coin_size = 20
coin_color = (255, 215, 0) # Gold color for coins (RGB)
num_coins = 10
coins = []

# 10. Score variable
score = 0

# Function to spawn a new coin at a random valid location
def spawn_coin():
    x = random.randint(coin_size, screen_width - coin_size)
    y = random.randint(coin_size, screen_height - coin_size)
    return pygame.Rect(x, y, coin_size, coin_size)

# Initialize coins
for _ in range(num_coins):
    coins.append(spawn_coin())


# 11. Game Loop
running = True
while running:
    if game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Press 'R' to restart
                    game_over = False
                    score = 0
                    logo_rect.center = (screen_width // 2, screen_height // 2) # Reset Spongebob
                    player_rect.centerx = screen_width // 2 # Reset player
                    player_rect.bottom = screen_height - 10
                    coins = [] # Clear and respawn coins
                    for _ in range(num_coins):
                        coins.append(spawn_coin())

        screen.blit(background_image, (0, 0))
        screen.blit(logo_image, logo_rect)
        screen.blit(player_image, player_rect)

        # Display "Game Over!" text
        game_over_text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(game_over_text, game_over_text_rect)

        # Display Final Score on Game Over screen
        final_score_text = font.render(f"Final Score: {score}", True, (255, 165, 0))
        final_score_text_rect = final_score_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))
        screen.blit(final_score_text, final_score_text_rect)

        restart_text = font.render("Press 'R' to Restart", True, (153, 50, 204))
        restart_text_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 70))
        screen.blit(restart_text, restart_text_rect)

        pygame.display.flip()
        clock.tick(FPS)
        continue

    # 12. Event Handling (Only when game is active)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 13. Player Input (Continuous Movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # 14. Keep Player within Screen Bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_width:
        player_rect.right = screen_width
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > screen_height:
        player_rect.bottom = screen_height

    # 15. Update Logo Position (Spongebob)
    logo_rect.x += dx
    logo_rect.y += dy

    # 16. Handle Bouncing off Edges for Spongebob
    if logo_rect.right >= screen_width or logo_rect.left <= 0:
        dx *= -1
    if logo_rect.bottom >= screen_height or logo_rect.top <= 0:
        dy *= -1

    # 17. Check for Collision between Spongebob and Player
    if logo_rect.colliderect(player_rect):
        print("COLLISION DETECTED! Game Over!")
        game_over = True

    # 18. Check for Player-Coin Collisions
    collected_coins = []
    for coin_rect in coins:
        if player_rect.colliderect(coin_rect):
            score += 1
            print(f"Coin collected! Score: {score}")
            collected_coins.append(coin_rect)

    for coin_rect in collected_coins:
        coins.remove(coin_rect)
        coins.append(spawn_coin())

    # 19. Drawing
    screen.blit(background_image, (0, 0))
    screen.blit(logo_image, logo_rect)
    screen.blit(player_image, player_rect)

    # Draw Coins
    for coin_rect in coins:
        pygame.draw.circle(screen, coin_color, coin_rect.center, coin_size // 2)

    # Display Current Score during game
    score_text = font.render(f"Score: {score}", True, (255, 165, 0))
    screen.blit(score_text, (10, 10))

    # 20. Update the display
    pygame.display.flip()

    # 21. Cap the frame rate
    clock.tick(FPS)

# 22. Quit Pygame
pygame.quit()
print("Game Over!")