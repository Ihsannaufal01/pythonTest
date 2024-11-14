
<h1 align='center'>Penjelasan code PingPong.py</h1>




<!-- 1. Inisialisasi Pygame dan Pengaturan Dasar -->

```
import pygame
import sys
```
<strong>pygame</strong>: Pustaka untuk membuat game.
<br>
<strong>sys</strong>: Digunakan untuk keluar dari program dengan sys.exit().
```
pygame.init()
```
Menginisialisasi semua modul Pygame yang diperlukan.
```
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
```
<strong>WIDTH</strong> dan <strong>HEIGHT</strong>: Ukuran layar game.
<br>
<strong>pygame.display.set_mode()</strong>: Membuat jendela dengan ukuran tertentu.
<br>
<strong>pygame.display.set_caption()</strong>: Menetapkan judul jendela.

<!-- 2. Definisi Warna -->
```
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
```
Warna dalam format RGB untuk elemen layar.

<!-- 3. Pengaturan Paddle dan Bola -->

```
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
```
<strong>PADDLE_WIDTH</strong> dan <strong>PADDLE_HEIGHT</strong>: Dimensi paddle.
<br>
<strong>paddle_speed</strong>: Kecepatan paddle bergerak.
<br>
<strong>pygame.Rect</strong>: Membuat objek persegi panjang untuk paddle kiri dan kanan.

```
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5
```
<strong>BALL_SIZE</strong>: Ukuran bola.
<br>
<strong>pygame.Rect</strong>: Membuat objek persegi panjang untuk bola.
<br>
<strong>ball_speed_x</strong> dan <strong>ball_speed_y</strong>: Kecepatan bola pada sumbu X dan Y.
<!-- 4. Skor dan Font -->

```
left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)
```
<strong>left_score</strong> dan <strong>right_score</strong>: Variabel untuk mencatat skor kedua pemain.
<br>
<strong>pygame.font.Font</strong>: Digunakan untuk membuat teks pada layar.
<!-- 5. Fungsi untuk Menggambar Elemen -->

```
def draw_elements():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))
```
<strong>screen.fill()</strong>: Mengisi layar dengan warna hitam.
<br>
<strong>pygame.draw.rect()</strong>: Menggambar paddle kiri dan kanan.
<br>
<strong>pygame.draw.ellipse()</strong>: Menggambar bola.
<br>
<strong>pygame.draw.aaline()</strong>: Menggambar garis tengah layar.
<br>
<strong>font.render()</strong>: Membuat teks untuk skor.
<br>
<strong>screen.blit()</strong>: Menampilkan teks skor ke layar.
<!-- 6. Fungsi Reset Bola -->

```
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global ball_speed_x, ball_speed_y
    ball_speed_x *= -1
    ball_speed_y *= -1
```
<strong>ball.center</strong>: Mengatur posisi bola kembali ke tengah layar.
<br>
<strong>ball_speed_x</strong>, <strong>dan ball_speed_y</strong>: Membalik arah bola saat di-reset.
<!-- 7. Game Loop -->
Event Handling
```
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
<strong>pygame.event.get()</strong>: Mengecek event seperti tombol keluar.
<br>
<strong>pygame.QUIT</strong>: Event saat pemain menutup game.
Input Pemain

```
keys = pygame.key.get_pressed()
if keys[pygame.K_w] and left_paddle.top > 0:
    left_paddle.y -= paddle_speed
if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
    left_paddle.y += paddle_speed
if keys[pygame.K_UP] and right_paddle.top > 0:
    right_paddle.y -= paddle_speed
if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
    right_paddle.y += paddle_speed
```
<strong>pygame.key.get_pressed()</strong>: Mengecek tombol yang ditekan.
<br>
Tombol Kontrol:
<br>
<strong>W / S</strong>: Menggerakkan paddle kiri.
<br>
<strong>Panah Atas</strong> / <strong>Panah Bawah</strong>: Menggerakkan paddle kanan.
Gerakan Bola

```
ball.x += ball_speed_x
ball.y += ball_speed_y
```
Mengupdate posisi bola berdasarkan kecepatannya.
<!-- Pantulan Bola -->

```
if ball.top <= 0 or ball.bottom >= HEIGHT:
    ball_speed_y *= -1

if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
    ball_speed_x *= -1
```
Bola memantul jika menyentuh tepi atas/bawah layar.
<br>
Bola memantul jika menyentuh paddle.
<!-- Reset dan Skor -->

```
if ball.left <= 0:
    right_score += 1
    reset_ball()

if ball.right >= WIDTH:
    left_score += 1
    reset_ball()
```
Menambah skor pemain lawan jika bola melewati paddle.
<br>
Memanggil fungsi <strong>reset_ball()</strong> untuk mengembalikan bola ke tengah.
Gambar Elemen dan Update Layar

```
draw_elements()
pygame.display.flip()
clock.tick(FPS)
```
<strong>draw_elements()</strong>: Memanggil fungsi untuk menggambar semua elemen.
<br>
<strong>pygame.display.flip()</strong>: Memperbarui layar.
<br>
<strong>clock.tick(FPS)</strong>: Mengatur kecepatan game (60 FPS).
<!-- 8. Keluar dari Game -->

```
pygame.quit()
sys.exit()
```
<strong>pygame.quit()</strong>: Menutup semua modul Pygame.
<strong>ys.exit()</strong>: Menghentikan program.
