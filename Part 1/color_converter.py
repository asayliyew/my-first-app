# Файл color.converter.py
# Автор: Сергеев Дмитрий Владимирович
# Этот файл является частью проетка 'hello-engineer'
# Вариант 7: Конвертер RGB в HEX

def rgb_to_hex(r, g, b):
    return f"#{r:02X}{g:02X}{b:02X}"

def run_converter():
    print("=== Конвертер RGB в HEX ===")
    r = int(input("Введите значение R (0-255): "))
    g = int(input("Введите значение G (0-255): "))
    b = int(input("Введите значение B (0-255): "))
        
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Ошибка: значения должны быть в диапазоне 0–255.")
            return
        
    hex_color = rgb_to_hex(r, g, b)
    print(f"\nRGB({r}, {g}, {b}) → HEX {hex_color}")

run_converter()