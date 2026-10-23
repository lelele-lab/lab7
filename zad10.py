import math

class Complex:
    """Класс, описывающий комплексное число (a + bi)."""

    def __init__(self, a, b):
        """Конструктор. a — действительная часть, b — мнимая."""
        self._a = a
        self._b = b

    #  Свойства (геттеры) 
    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    #  Методы 

    def __add__(self, other):
        """Сложение: (a1 + b1i) + (a2 + b2i) = (a1+a2) + (b1+b2)i."""
        return Complex(self._a + other.a, self._b + other.b)

    def __mul__(self, other):
        """Умножение: (a1 + b1i)(a2 + b2i) = (a1a2 - b1b2) + (a1b2 + b1a2)i."""
        # Раскрываем скобки по правилам математики
        novaya_a = self._a * other.a - self._b * other.b
        novaya_b = self._a * other.b + self._b * other.a
        return Complex(novaya_a, novaya_b)

    def modul(self):
        """Модуль комплексного числа: √(a² + b²)."""
        return math.sqrt(self._a ** 2 + self._b ** 2)

    def info(self):
        """Красивый вывод числа."""
        # Если b положительное, ставим плюс, если отрицательное — минус сам покажется
        if self._b >= 0:
            print(f"{self._a} + {self._b}i")
        else:
            print(f"{self._a} - {abs(self._b)}i")


# ВВОД 

def vvod_kompleksnogo(nomer):
    """Спрашивает a и b и создает комплексное число."""
    print(f"\nВведите {nomer}-е комплексное число (a + bi):")
    try:
        a = float(input("  a = "))
        b = float(input("  b = "))
        return Complex(a, b)
    except ValueError:
        print("Ошибка: нужно ввести числа.")
        return None


# ГЛАВНАЯ ПРОГРАММА

def main():
    c1 = None
    c2 = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Задать первое число (a + bi)")
        print("2 - Задать второе число (a + bi)")
        print("3 - Показать числа")
        print("4 - Сложить числа (+)")
        print("5 - Умножить числа (*)")
        print("6 - Модуль первого числа")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            c1 = vvod_kompleksnogo(1)
        elif vibor == "2":
            c2 = vvod_kompleksnogo(2)

        elif vibor == "3":
            if c1:
                print("Первое число: ", end="")
                c1.info()
            else:
                print("Первое число не задано.")
            if c2:
                print("Второе число: ", end="")
                c2.info()
            else:
                print("Второе число не задано.")

        elif vibor == "4":
            if c1 and c2:
                print("Результат сложения: ", end="")
                # Благодаря __add__ работает вот так:
                (c1 + c2).info()
            else:
                print("Сначала задайте оба числа!")

        elif vibor == "5":
            if c1 and c2:
                print("Результат умножения: ", end="")
                # Благодаря __mul__ работает вот так:
                (c1 * c2).info()
            else:
                print("Сначала задайте оба числа!")

        elif vibor == "6":
            if c1:
                print(f"Модуль первого числа: {round(c1.modul(), 4)}")
            else:
                print("Первое число не задано.")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()