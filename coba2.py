import pygame
# Mengimpor Pygame

#Menginisialisasi semua modul Pygame
pygame.init()

# Menentukan ukuran jendela
screen = pygame.display.set_mode((800, 600))

# Menetapkan judul jendela
pygame.display.set_caption("Contoh Pygame: Gambar dan Suara")

# Memuat gambar
gambar = pygame.image.load("bg.png") 
# Pastikan gambar.png ada didirektori yang sama

# Memuat musik dengan Pygame Mixer
pygame.mixer.init() # Menginisialisasi mixer
pygame.mixer.music.load("Pasilyo.mp3") # Pastikan musik.mp3 ada di direktori yang sama

# Memulai pemutaran musik
pygame.mixer.music.play(-1) # Memutar musik secara berulang

# Mengatur kecepatan frame
clock = pygame.time.Clock()

# Program utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Menggambar gambar pada layar
screen.fill((255, 255, 255)) # Mengisi layar dengan warna putih
screen.blit(gambar, (100, 100)) # Menampilkan gambar pada posisi (100,100)

# Memperbarui tampilan layar
pygame.display.update()

# Mengatur frame rate
clock.tick(60)

# Menghentikan musik dan keluar dari program
pygame.mixer.music.stop()
pygame.quit()