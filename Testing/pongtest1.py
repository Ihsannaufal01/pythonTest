import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Simple")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Objek paddle dan bola
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Kecepatan bola dan paddle
ball_speed_x = 5
ball_speed_y = 5
paddle_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    # Gerakan bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Pantulan bola
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Reset posisi bola jika keluar
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Gambar elemen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Update layar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
