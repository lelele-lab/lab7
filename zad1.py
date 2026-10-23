class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title, author, year, price):
        """Конструктор с защитой данных."""
        self.__title = title
        self.__author = author
        self.__year = year
        # Инкапсуляция: цена не может быть отрицательной
        if price < 0:
            print("Цена не может быть отрицательной. Установлен 0.")
            self.__price = 0
        else:
            self.__price = price

    # Свойства (геттеры) 
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def price(self):
        return self.__price

    # Методы 
    def apply_discount(self, percent):
        """Применяет скидку к цене."""
        if percent < 0 or percent > 100:
            print("Ошибка: скидка должна быть от 0 до 100%.")
        else:
            self.__price = self.__price * (1 - percent / 100)
            print(f"Скидка {percent}% применена. Новая цена: {round(self.__price, 2)} руб.")

    def compare_price(self, other):
        """Сравнивает цену с другой книгой."""
        if self.__price == other.price:
            print("Книги стоят одинаково.")
        elif self.__price < other.price:
            print(f"'{self.__title}' дешевле, чем '{other.title}'.")
        else:
            print(f"'{self.__title}' дороже, чем '{other.title}'.")

    def display_info(self):
        """Выводит информацию о книге."""
        print(f"'{self.__title}' ({self.__author}), {self.__year} г. - {round(self.__price, 2)} руб.")


# ВВОД И МЕНЮ

def vvod_knigi():
    """Спрашивает данные и возвращает объект Book."""
    n = input("Название: ")
    a = input("Автор: ")
    while True:
        try:
            g = int(input("Год: "))
            break
        except ValueError:
            print("Ошибка: год должен быть числом.")
    
    while True:
        try:
            c = float(input("Цена: "))
            break
        except ValueError:
            print("Ошибка: цена должна быть числом.")
            
    return Book(n, a, g, c)


def main():
    """Главное меню программы."""
    biblioteka = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить книгу")
        print("2 - Показать все книги")
        print("3 - Применить скидку к книге")
        print("4 - Сравнить две книги")
        print("0 - Выход")
        
        vibor = input("Выбор: ")

        if vibor == "1":
            biblioteka.append(vvod_knigi())
            print("Книга добавлена!")

        elif vibor == "2":
            if not biblioteka:
                print("Библиотека пуста.")
            else:
                for i, kniga in enumerate(biblioteka):
                    print(f"[{i}] ", end="")
                    kniga.display_info()

        elif vibor == "3":
            if not biblioteka:
                print("Сначала добавьте книги!")
                continue
            for i, kniga in enumerate(biblioteka):
                print(f"[{i}] ", end="")
                kniga.display_info()
            try:
                idx = int(input("К какой книге применить скидку? (введите номер): "))
                p = float(input("Размер скидки в %: "))
                biblioteka[idx].apply_discount(p)
            except (ValueError, IndexError):
                print("Ошибка: неверный номер книги или размер скидки.")

        elif vibor == "4":
            if len(biblioteka) < 2:
                print("Для сравнения нужно минимум две книги.")
                continue
            for i, kniga in enumerate(biblioteka):
                print(f"[{i}] ", end="")
                kniga.display_info()
            try:
                idx1 = int(input("Номер первой книги: "))
                idx2 = int(input("Номер второй книги: "))
                biblioteka[idx1].compare_price(biblioteka[idx2])
            except (ValueError, IndexError):
                print("Ошибка: неверный номер книги.")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()