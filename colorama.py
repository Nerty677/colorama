import colorama
from colorama import init, deinit, Cursor

# Ініціалізація Colorama
init(autoreset=True)


def print_custom_message():
    print("Це стандартний текст без кольору.")
    print("Ще один рядок звичайного тексту.")


def reset_colors():
    print("Тепер кольори мають бути скинуті.")


def move_cursor():
    print(Cursor.UP(2) + "Курсор переміщено на дві строки вгору")
    print(Cursor.FORWARD(10) + "Курсор переміщено на десять позицій вперед")
    print(Cursor.BACK(5) + "Курсор переміщено на п'ять позицій назад")
    print(Cursor.DOWN(3) + "Курсор переміщено на три строки вниз")


def advanced_printing():
    for i in range(5):
        print(f"{Cursor.POS(i + 1, i + 1)} Позиція курсору: ({i + 1}, {i + 1})")


def show_demo():
    print("=== Демонстрація Colorama ===")
    print_custom_message()
    reset_colors()
    move_cursor()
    advanced_printing()


# Виклик функцій для демонстрації
show_demo()

# Завершення роботи з Colorama
deinit()
