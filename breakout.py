import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 149, 221)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI-Powered Breakout")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - 20
paddle_speed = 7

# Ball settings
BALL_RADIUS = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = random.choice([-4, 4])
ball_dy = -4

# Brick settings
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_PADDING = 10
BRICK_OFFSET_TOP = 30
BRICK_OFFSET_LEFT = 30

# Create bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        brick_x = BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING)
        brick_y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

# AI settings
ai_enabled = True

# Main game loop
def main():
    global paddle_x, ball_x, ball_y, ball_dx, ball_dy

    running = True

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement (player or AI)
        keys = pygame.key.get_pressed()
        if not ai_enabled:
            if keys[pygame.K_LEFT] and paddle_x > 0:
                paddle_x -= paddle_speed
            if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
                paddle_x += paddle_speed
        else:
            # AI control: Move paddle to align with the ball
            target_x = ball_x - PADDLE_WIDTH // 2
            if paddle_x < target_x and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
                paddle_x += paddle_speed
            elif paddle_x > target_x and paddle_x > 0:
                paddle_x -= paddle_speed

        # Ball movement
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with walls
        if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball_y - BALL_RADIUS <= 0:
            ball_dy = -ball_dy
        elif ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
            print("Game Over!")
            running = False

        # Ball collision with paddle
        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle_rect.collidepoint(ball_x, ball_y):
            ball_dy = -ball_dy

        # Ball collision with bricks
        for brick in bricks[:]:
            if brick.collidepoint(ball_x, ball_y):
                bricks.remove(brick)
                ball_dy = -ball_dy
                break

        # Draw bricks
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        # Draw paddle
        pygame.draw.rect(screen, BLUE, paddle_rect)

        # Draw ball
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

        # Check for win condition
        if not bricks:
            print("You Win!")
            running = False

        # Update the display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
