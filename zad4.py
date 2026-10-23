class Point:
    """Класс для точки с координатами x и y."""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def info(self):
        return f"({self._x}; {self._y})"


class Rectangle:
    """Класс прямоугольника, заданного двумя противоположными точками."""

    def __init__(self, p1, p2):
        """Конструктор принимает две точки."""
        self._p1 = p1
        self._p2 = p2

    #  Свойства (вычисляем ширину и высоту на лету) 
    @property
    def shirina(self):
        """Ширина — это разница по X."""
        return abs(self._p1.x - self._p2.x)

    @property
    def vysota(self):
        """Высота — это разница по Y."""
        return abs(self._p1.y - self._p2.y)

    #  Методы 
    def ploshad(self):
        """Площадь: ширина * высота."""
        return self.shirina * self.vysota

    def perimetr(self):
        """Периметр: 2 * (ширина + высота)."""
        return 2 * (self.shirina + self.vysota)

    def peresechenie(self, other):
        """Проверяет, пересекается ли текущий прямоугольник с другим."""
        # Находим крайние точки (левый низ и правый верх) для обоих прямоугольников
        # Для текущего:
        my_min_x = min(self._p1.x, self._p2.x)
        my_max_x = max(self._p1.x, self._p2.x)
        my_min_y = min(self._p1.y, self._p2.y)
        my_max_y = max(self._p1.y, self._p2.y)

        # Для другого:
        other_min_x = min(other._p1.x, other._p2.x)
        other_max_x = max(other._p1.x, other._p2.x)
        other_min_y = min(other._p1.y, other._p2.y)
        other_max_y = max(other._p1.y, other._p2.y)

        # Условие пересечения: они не должны находиться строго друг от друга по осям
        if (my_min_x < other_max_x and my_max_x > other_min_x and
            my_min_y < other_max_y and my_max_y > other_min_y):
            return True
        return False

    def info(self):
        """Выводит информацию о прямоугольнике."""
        print(f"Прямоугольник с точками {self._p1.info()} и {self._p2.info()}")
        print(f"Ширина: {self.shirina}, Высота: {self.vysota}")


# ВВОД 

def vvod_tochki(nomer):
    """Спрашивает координаты точки."""
    try:
        print(f"Введите координаты {nomer}-й точки:")
        x = float(input("  x = "))
        y = float(input("  y = "))
        return Point(x, y)
    except ValueError:
        print("Ошибка: нужно ввести числа.")
        return None


def vvod_pryamougolnika(nomer):
    """Спрашивает две точки и создает прямоугольник."""
    print(f"\n--- Создание {nomer}-го прямоугольника ---")
    p1 = vvod_tochki("первой")
    p2 = vvod_tochki("второй")
    if p1 and p2:
        return Rectangle(p1, p2)
    return None


# ГЛАВНАЯ ПРОГРАММА 

def main():
    pryam1 = None
    pryam2 = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Создать первый прямоугольник")
        print("2 - Создать второй прямоугольник")
        print("3 - Показать площадь и периметр")
        print("4 - Проверить на пересечение")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            pryam1 = vvod_pryamougolnika(1)

        elif vibor == "2":
            pryam2 = vvod_pryamougolnika(2)

        elif vibor == "3":
            if pryam1:
                print("\n[Первый прямоугольник]")
                pryam1.info()
                print(f"Площадь: {pryam1.ploshad()}")
                print(f"Периметр: {pryam1.perimetr()}")
            else:
                print("Первый прямоугольник еще не создан.")

            if pryam2:
                print("\n[Второй прямоугольник]")
                pryam2.info()
                print(f"Площадь: {pryam2.ploshad()}")
                print(f"Периметр: {pryam2.perimetr()}")
            else:
                print("Второй прямоугольник еще не создан.")

        elif vibor == "4":
            if pryam1 and pryam2:
                if pryam1.peresechenie(pryam2):
                    print("Прямоугольники ПЕРЕСЕКАЮТСЯ.")
                else:
                    print("Прямоугольники НЕ пересекаются.")
            else:
                print("Сначала создайте оба прямоугольника.")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()
