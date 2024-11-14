
<h1 align='center'>Penjelasan code PingPong.py</h1>




<!-- 1. Inisialisasi Pygame dan Pengaturan Dasar -->

```
import pygame
import sys
```
`pygame`: Pustaka untuk membuat game.
<br>
`sys`: Digunakan untuk keluar dari program dengan sys.exit().
```
pygame.init()
```
Menginisialisasi semua modul Pygame yang diperlukan.
```
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
```
`WIDTH` dan `HEIGHT`: Ukuran layar game.
<br>
`pygame.display.set_mode()`: Membuat jendela dengan ukuran tertentu.
<br>
`pygame.display.set_caption()`: Menetapkan judul jendela.

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
`PADDLE_WIDTH` dan `PADDLE_HEIGHT`: Dimensi paddle.
<br>
`paddle_speed`: Kecepatan paddle bergerak.
<br>
`pygame.Rect`: Membuat objek persegi panjang untuk paddle kiri dan kanan.

```
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5
```
`BALL_SIZE`: Ukuran bola.
<br>
`pygame.Rect`: Membuat objek persegi panjang untuk bola.
<br>
`ball_speed_x` dan `ball_speed_y`: Kecepatan bola pada sumbu X dan Y.
<!-- 4. Skor dan Font -->

```
left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)
```
`left_score` dan `right_score`: Variabel untuk mencatat skor kedua pemain.
<br>
`pygame.font.Font`: Digunakan untuk membuat teks pada layar.
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
`screen.fill()`: Mengisi layar dengan warna hitam.
<br>
`pygame.draw.rect()`: Menggambar paddle kiri dan kanan.
<br>
`pygame.draw.ellipse()`: Menggambar bola.
<br>
`pygame.draw.aaline()`: Menggambar garis tengah layar.
<br>
`font.render()`: Membuat teks untuk skor.
<br>
`screen.blit()`: Menampilkan teks skor ke layar.
<!-- 6. Fungsi Reset Bola -->

```
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global ball_speed_x, ball_speed_y
    ball_speed_x *= -1
    ball_speed_y *= -1
```
`ball.center`: Mengatur posisi bola kembali ke tengah layar.
<br>
`ball_speed_x`, `dan ball_speed_y`: Membalik arah bola saat di-reset.
<!-- 7. Game Loop -->
<!-- Event Handling -->
```
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
`pygame.event.get()`: Mengecek event seperti tombol keluar.
<br>
`pygame.QUIT`: Event saat pemain menutup game.
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
`pygame.key.get_pressed()`: Mengecek tombol yang ditekan.
<br>
Tombol Kontrol:
<br>
`W / S`: Menggerakkan paddle kiri.
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
Memanggil fungsi `reset_ball()` untuk mengembalikan bola ke tengah.
Gambar Elemen dan Update Layar

```
draw_elements()
pygame.display.flip()
clock.tick(FPS)
```
`draw_elements()`: Memanggil fungsi untuk menggambar semua elemen.
<br>
`pygame.display.flip()`: Memperbarui layar.
<br>
`clock.tick(FPS)`: Mengatur kecepatan game (60 FPS).
<!-- 8. Keluar dari Game -->

```
pygame.quit()
sys.exit()
```
`pygame.quit()`: Menutup semua modul Pygame.
<br>
`ys.exit()`: Menghentikan program.

```
paddle_bounce_sound = pygame.mixer.Sound("paddle_bounce.wav")
```
File suara dimuat ke dalam program. Pastikan file suara `paddle_bounce.wav` ada di direktori yang sama.
Memainkan Suara:

```
if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
    ball_speed_x *= -1
    paddle_bounce_sound.play()
```
Bola hanya memainkan suara `paddle_bounce_sound` saat menyentuh paddle kiri atau kanan.
Dinding Tidak Memainkan Suara:

Bola yang memantul dari dinding atas atau bawah tidak memainkan suara.