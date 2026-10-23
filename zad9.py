class Temperature:
    """Класс, описывающий температуру и её шкалу."""

    def __init__(self, znachenie, shkala):
        """Конструктор с проверкой данных (инкапсуляция)."""
        self._znachenie = znachenie
        # Приводим шкалу к верхнему регистру (чтобы 'c' и 'C' работали одинаково)
        shkala = shkala.upper() 
        
        if shkala not in ["C", "F", "K"]:
            print("Ошибка: неизвестная шкала. Установлен Цельсий (C).")
            self._shkala = "C"
        else:
            self._shkala = shkala

        # Защита от физически невозможных значений (ниже абсолютного нуля)
        if self._shkala == "K" and znachenie < 0:
            print("Ошибка: Кельвин не может быть отрицательным. Установлен 0.")
            self._znachenie = 0.0
        elif self._shkala == "C" and znachenie < -273.15:
            print("Ошибка: ниже абсолютного нуля. Установлен -273.15.")
            self._znachenie = -273.15
        elif self._shkala == "F" and znachenie < -459.67:
            print("Ошибка: ниже абсолютного нуля. Установлен -459.67.")
            self._znachenie = -459.67

    # Свойства (геттеры) 
    @property
    def znachenie(self):
        return self._znachenie

    @property
    def shkala(self):
        return self._shkala

    # Методы конвертации

    def v_celsiy(self):
        """Переводит текущую температуру в Цельсий (внутренний стандарт)."""
        if self._shkala == "C":
            return self._znachenie
        elif self._shkala == "F":
            return (self._znachenie - 32) * 5 / 9
        elif self._shkala == "K":
            return self._znachenie - 273.15

    def konvertirovat(self, novaya_shkala):
        """Конвертирует температуру в новую шкалу и возвращает новый объект Temperature."""
        novaya_shkala = novaya_shkala.upper()
        
        # Сначала получаем значение в Цельсиях
        c = self.v_celsiy()

        # Теперь переводим из Цельсия в нужную шкалу
        if novaya_shkala == "C":
            return Temperature(c, "C")
        elif novaya_shkala == "F":
            return Temperature(c * 9 / 5 + 32, "F")
        elif novaya_shkala == "K":
            return Temperature(c + 273.15, "K")
        else:
            print("Ошибка: неизвестная шкала для конвертации.")
            return None

    def info(self):
        """Выводит температуру."""
        # Красивое отображение шкалы
        nazvanie = {"C": "°C", "F": "°F", "K": "K"}
        print(f"{round(self._znachenie, 2)} {nazvanie[self._shkala]}")


# ВВОД 

def vvod_temperatury():
    """Спрашивает температуру и шкалу."""
    try:
        znachenie = float(input("Введите значение температуры: "))
    except ValueError:
        print("Ошибка: значение должно быть числом.")
        return None
        
    shkala = input("Введите шкалу (C, F, K): ")
    return Temperature(znachenie, shkala)


# ГЛАВНАЯ ПРОГРАММА

def main():
    temp = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Задать температуру")
        print("2 - Показать текущую температуру")
        print("3 - Конвертировать в Цельсий (C)")
        print("4 - Конвертировать в Фаренгейт (F)")
        print("5 - Конвертировать в Кельвин (K)")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            temp = vvod_temperatury()
            if temp:
                print("Температура задана.")

        elif vibor == "2":
            if temp:
                print("Текущая температура: ", end="")
                temp.info()
            else:
                print("Температура не задана.")

        elif vibor in ["3", "4", "5"]:
            if temp:
                if vibor == "3":
                    novaya = temp.konvertirovat("C")
                elif vibor == "4":
                    novaya = temp.konvertirovat("F")
                else:
                    novaya = temp.konvertirovat("K")
                
                if novaya:
                    print("Результат конвертации: ", end="")
                    novaya.info()
            else:
                print("Сначала задайте температуру!")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()