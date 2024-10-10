import os
import time

def print_flag():
    green = "\033[42m"  # зелёный фон
    red = "\033[41m"    # красный фон
    reset = "\033[0m"   # сброс цвета

    # Размеры флага
    height = 8
    width = 20
    square_size = 4
    square_start_row = (height - square_size) // 2  # Центрируем квадрат по вертикали
    square_start_col = (width - square_size) // 2  # Центрируем квадрат по горизонтали

    for row in range(height):
        for col in range(width):
            if square_start_row <= row < square_start_row + square_size and square_start_col <= col < square_start_col + square_size:
                print(red + "  ", end="")  # Квадрат красного цвета
            else:
                print(green + "  ", end="")  # Зелёный фон
        print(reset)

def animate_flag():
    for _ in range(3):  # 3 кадра
        os.system('cls' if os.name == 'nt' else 'clear')
        print_flag()
        time.sleep(0.5)  # Задержка между кадрами

animate_flag()