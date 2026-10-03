# Pacman Game 🎮

Game Pacman sederhana yang dibuat menggunakan **Python** dan library **Pygame**.

Project ini dibuat sebagai latihan pemrograman game menggunakan Python, dengan menerapkan konsep seperti pergerakan karakter, maze, collision, pellet, dan enemy.

## 🕹️ Fitur

- Pergerakan karakter Pacman menggunakan keyboard
- Maze sebagai arena permainan
- Pellet yang dapat dikumpulkan
- Enemy yang mengejar atau bergerak di dalam maze
- Collision antara Pacman, dinding, pellet, dan enemy
- Sistem skor
- Game Over ketika Pacman terkena enemy

## 🛠️ Teknologi

- **Python**
- **Pygame**

## 📁 Struktur Project

```text
Pacman/
├── main.py
└── README.md
```

> Struktur folder dapat berbeda tergantung aset yang digunakan dalam project.

## ⚙️ Instalasi

Pastikan Python sudah terinstall di komputer.

Kemudian install Pygame dengan:

```bash
pip install pygame
```

## ▶️ Cara Menjalankan

Clone repository:

```bash
git clone https://github.com/USERNAME/NAMA-REPOSITORY.git
```

Masuk ke folder project:

```bash
cd Pacman
```

Jalankan game:

```bash
python main.py
```

## 🎮 Kontrol

| Tombol | Fungsi |
|---|---|
| ⬆️ Arrow Up | Bergerak ke atas |
| ⬇️ Arrow Down | Bergerak ke bawah |
| ⬅️ Arrow Left | Bergerak ke kiri |
| ➡️ Arrow Right | Bergerak ke kanan |
| `Space` | Memulai game |

## 🎯 Tujuan Game

Tujuan utama game adalah mengendalikan Pacman untuk mengumpulkan seluruh pellet di dalam maze sambil menghindari enemy.

Pemain mendapatkan skor dengan mengumpulkan pellet. Permainan berakhir ketika Pacman terkena enemy.

## 📚 Pembelajaran

Project ini dibuat untuk mempelajari dan memahami:

- Dasar penggunaan Python
- Game loop dengan Pygame
- Event handling
- Pergerakan karakter
- Collision detection
- Penggunaan array/grid untuk membuat maze
- Sistem skor
- Logika pergerakan enemy
