import math

class Vector2D:
    """Класс, описывающий двумерный вектор (x, y)."""

    def __init__(self, x, y):
        """Конструктор с инкапсуляцией."""
        self._x = x
        self._y = y

    #  Свойства (геттеры) 
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Методы 
    
    #  метод для сложения: v1 + v2
    def __add__(self, other):
        """Сложение векторов."""
        return Vector2D(self._x + other.x, self._y + other.y)

    # метод для вычитания: v1 - v2
    def __sub__(self, other):
        """Вычитание векторов."""
        return Vector2D(self._x - other.x, self._y - other.y)

    def dlina(self):
        """Длина вектора (модуль) по теореме Пифагора."""
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def skalarnoe_proizvedenie(self, other):
        """Скалярное произведение: x1*x2 + y1*y2."""
        return self._x * other.x + self._y * other.y

    def info(self):
        """Выводит вектор в формате (x; y)."""
        print(f"({self._x}; {self._y})")


# ВВОД 

def vvod_vektora(nomer):
    """Спрашивает координаты и создает вектор."""
    print(f"\nВведите координаты {nomer}-го вектора:")
    try:
        x = float(input("  x = "))
        y = float(input("  y = "))
        return Vector2D(x, y)
    except ValueError:
        print("Ошибка: нужно ввести числа.")
        return None


# ГЛАВНАЯ ПРОГРАММА

def main():
    v1 = None
    v2 = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Задать первый вектор")
        print("2 - Задать второй вектор")
        print("3 - Показать векторы")
        print("4 - Сложить векторы (+)")
        print("5 - Вычесть векторы (-)")
        print("6 - Длина первого вектора")
        print("7 - Скалярное произведение")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            v1 = vvod_vektora(1)
        elif vibor == "2":
            v2 = vvod_vektora(2)

        elif vibor == "3":
            if v1:
                print("Первый вектор: ", end="")
                v1.info()
            else:
                print("Первый вектор не задан.")
            if v2:
                print("Второй вектор: ", end="")
                v2.info()
            else:
                print("Второй вектор не задан.")

        elif vibor == "4":
            if v1 and v2:
                print("Результат сложения: ", end="")
                # Благодаря __add__ мы можем просто написать v1 + v2
                (v1 + v2).info()
            else:
                print("Сначала задайте оба вектора!")

        elif vibor == "5":
            if v1 and v2:
                print("Результат вычитания: ", end="")
                # Благодаря __sub__ мы можем написать v1 - v2
                (v1 - v2).info()
            else:
                print("Сначала задайте оба вектора!")

        elif vibor == "6":
            if v1:
                print(f"Длина первого вектора: {round(v1.dlina(), 4)}")
            else:
                print("Первый вектор не задан.")

        elif vibor == "7":
            if v1 and v2:
                print(f"Скалярное произведение: {round(v1.skalarnoe_proizvedenie(v2), 4)}")
            else:
                print("Сначала задайте оба вектора!")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()