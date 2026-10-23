class Time:
    """Класс, описывающий время (часы, минуты, секунды)."""

    def __init__(self, chasy, minuty, sekundy):
        """Конструктор с защитой данных (инкапсуляция)."""
        # Проверяем, чтобы значения были в нормальных пределах
        if chasy < 0 or minuty < 0 or sekundy < 0:
            print("Ошибка: время не может быть отрицательным. Установлен 0.")
            self._chasy, self._minuty, self._sekundy = 0, 0, 0
        else:
            # Переводим всё в секунды для хранения
            self._vsego_sekund = chasy * 3600 + minuty * 60 + sekundy

    # Свойства 
    @property
    def chasy(self):
        # Делим общее количество секунд на 3600 (секунд в часе)
        return (self._vsego_sekund // 3600) % 24 # Ограничиваем 24 часами

    @property
    def minuty(self):
        return (self._vsego_sekund % 3600) // 60

    @property
    def sekundy(self):
        return self._vsego_sekund % 60

    @property
    def vsego_sekund(self):
        return self._vsego_sekund

    # Методы 
    def slozhenie(self, other):
        """Сложение двух времен."""
        obshie_sekundy = self._vsego_sekund + other.vsego_sekund
        # Создаем новый объект на основе общего количества секунд
        return Time(obshie_sekundy // 3600, (obshie_sekundy % 3600) // 60, obshie_sekundy % 60)

    def raznica(self, other):
        """Разница между двумя временами (по модулю)."""
        raznica_sek = abs(self._vsego_sekund - other.vsego_sekund)
        return Time(raznica_sek // 3600, (raznica_sek % 3600) // 60, raznica_sek % 60)

    def sravnenie(self, other):
        """Сравнение двух времен. Возвращает 1 (больше), -1 (меньше) или 0 (равно)."""
        if self._vsego_sekund > other.vsego_sekund:
            return 1
        elif self._vsego_sekund < other.vsego_sekund:
            return -1
        else:
            return 0

    def info(self):
        """Красивый вывод времени."""
        # :02d означает, что если число меньше 10, добавится ноль спереди (например, 05)
        print(f"{self.chasy:02d}:{self.minuty:02d}:{self.sekundy:02d}")


# ВВОД

def vvod_vremeni(nomer):
    """Спрашивает время и создает объект Time."""
    print(f"\nВведите {nomer}-е время:")
    try:
        ch = int(input("  Часы: "))
        mi = int(input("  Минуты: "))
        se = int(input("  Секунды: "))
        return Time(ch, mi, se)
    except ValueError:
        print("Ошибка: нужно вводить целые числа.")
        return None


# ГЛАВНАЯ ПРОГРАММА

def main():
    vremya1 = None
    vremya2 = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Задать первое время")
        print("2 - Задать второе время")
        print("3 - Показать заданные времена")
        print("4 - Сложить времена")
        print("5 - Найти разницу")
        print("6 - Сравнить времена")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            vremya1 = vvod_vremeni(1)
        elif vibor == "2":
            vremya2 = vvod_vremeni(2)

        elif vibor == "3":
            if vremya1:
                print("Первое время: ", end="")
                vremya1.info()
            else:
                print("Первое время не задано.")
            if vremya2:
                print("Второе время: ", end="")
                vremya2.info()
            else:
                print("Второе время не задано.")

        elif vibor == "4":
            if vremya1 and vremya2:
                print("Результат сложения: ", end="")
                vremya1.slozhenie(vremya2).info()
            else:
                print("Сначала задайте оба времени!")

        elif vibor == "5":
            if vremya1 and vremya2:
                print("Разница: ", end="")
                vremya1.raznica(vremya2).info()
            else:
                print("Сначала задайте оба времени!")

        elif vibor == "6":
            if vremya1 and vremya2:
                res = vremya1.sravnenie(vremya2)
                if res == 1:
                    print("Первое время больше.")
                elif res == -1:
                    print("Второе время больше.")
                else:
                    print("Времена равны.")
            else:
                print("Сначала задайте оба времени!")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()