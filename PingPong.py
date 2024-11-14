import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kecepatan frame
FPS = 60
clock = pygame.time.Clock()

# Objek paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7

left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Bola
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Skor
left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)

# Suara
pygame.mixer.init()
paddle_bounce_sound = pygame.mixer.Sound("rubberballbouncing.wav")  # Ganti dengan file suara yang sesuai

# Fungsi untuk menggambar elemen
def draw_elements():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Tampilkan skor
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

# Fungsi untuk mengatur ulang bola
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global ball_speed_x, ball_speed_y
    ball_speed_x *= -1
    ball_speed_y *= -1

# Game loop
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

    # Pantulan bola di dinding atas/bawah
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Pantulan bola pada paddle
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
        paddle_bounce_sound.play()  # Mainkan suara saat bola menyentuh paddle

    # Skor
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # Gambar elemen
    draw_elements()

    # Update layar
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
