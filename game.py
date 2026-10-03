import pygame
import sys
import time


# Inisialisasi Pygame
pygame.init()

# Konstanta
CELL_SIZE = 40
ROWS = 10
COLS = 15
SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE
FPS = 10

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Labirin sederhana (1 = dinding, 0 = jalan, 2 = pintu keluar)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Posisi musuh (obstacles)
enemies = [[3, 3]]


# Fungsi untuk menggerakkan musuh secara acak
def move_enemies():
    for i, enemy in enumerate(enemies):

        directions = [
            (-1, 0),  # Atas
            (1, 0),   # Bawah
            (0, -1),  # Kiri
            (0, 1)    # Kanan
        ]

        import random
        random.shuffle(directions)

        possible_moves = []

        for dx, dy in directions:
            new_row = enemy[0] + dx
            new_col = enemy[1] + dy

            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                if MAZE[new_row][new_col] == 0:
                    possible_moves.append([new_row, new_col])

        if possible_moves:
            enemies[i] = random.choice(possible_moves)


# Fungsi untuk menggambar labirin
def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            if MAZE[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif MAZE[row][col] == 2:
                pygame.draw.rect(screen, RED, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Fungsi untuk menggambar pellet
def draw_pellets(pellets):
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, (pellet[1] * CELL_SIZE + CELL_SIZE // 2, pellet[0] * CELL_SIZE + CELL_SIZE // 2), 5)

# Fungsi untuk menggambar musuh
def draw_enemies():
    for enemy in enemies:
        pygame.draw.circle(screen, GREEN, (enemy[1] * CELL_SIZE + CELL_SIZE // 2, enemy[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)


# Fungsi untuk layar start
def start_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render("Press SPACE to Start", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

    # Tunggu hingga pemain menekan SPACE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

# Inisialisasi game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man with Moving Enemies")
clock = pygame.time.Clock()

# Posisi awal Pac-Man
player_pos = [1, 1]

# Pengaturan kecepatan Pac-Man
last_move_time = 0
move_delay = 0.10

# Daftar pellet
pellets = [[row, col] for row in range(ROWS) for col in range(COLS) if MAZE[row][col] == 0]

# Tampilkan layar start
start_screen()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dapatkan input dari pemain
    keys = pygame.key.get_pressed()
    current_time = time.time()

    if current_time - last_move_time >= move_delay:
        if keys[pygame.K_UP]:
            new_pos = [player_pos[0] - 1, player_pos[1]]
        elif keys[pygame.K_DOWN]:
            new_pos = [player_pos[0] + 1, player_pos[1]]
        elif keys[pygame.K_LEFT]:
            new_pos = [player_pos[0], player_pos[1] - 1]
        elif keys[pygame.K_RIGHT]:
            new_pos = [player_pos[0], player_pos[1] + 1]
        else:
            new_pos = player_pos

        # Periksa apakah posisi baru valid
        if MAZE[new_pos[0]][new_pos[1]] != 1:
            player_pos = new_pos
            last_move_time = current_time

    # Pindahkan musuh
    move_enemies()

    # Periksa tabrakan dengan musuh
    if player_pos in enemies:
        print("Game Over! You were caught by an enemy.")
        pygame.quit()
        sys.exit()

    # Periksa apakah Pac-Man mencapai pintu keluar
    if MAZE[player_pos[0]][player_pos[1]] == 2:
        print("Congratulations! You reached the exit.")
        pygame.quit()
        sys.exit()

    # Hapus pellet jika Pac-Man melewatinya
    if player_pos in pellets:
        pellets.remove(player_pos)

    # Gambar semua elemen di layar
    screen.fill(BLACK)
    draw_maze()
    draw_pellets(pellets)
    draw_enemies()
    pygame.draw.circle(screen, YELLOW, (player_pos[1] * CELL_SIZE + CELL_SIZE // 2, player_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    
    pygame.display.flip()
    clock.tick(FPS)