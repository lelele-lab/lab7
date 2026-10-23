class Product:
    """Класс, описывающий товар."""

    def __init__(self, nazvanie, kategoriya, cena, kolichestvo):
        """Конструктор с проверкой данных (инкапсуляция)."""
        self._nazvanie = nazvanie
        self._kategoriya = kategoriya
        
        # Защита: цена и количество не могут быть отрицательными
        if cena < 0:
            print("Цена не может быть отрицательной. Установлен 0.")
            self._cena = 0.0
        else:
            self._cena = cena

        if kolichestvo < 0:
            print("Количество не может быть отрицательным. Установлен 0.")
            self._kolichestvo = 0
        else:
            self._kolichestvo = kolichestvo

    # Свойства (геттеры) 
    @property
    def nazvanie(self):
        return self._nazvanie

    @property
    def kategoriya(self):
        return self._kategoriya

    @property
    def cena(self):
        return self._cena

    @property
    def kolichestvo(self):
        return self._kolichestvo

    # Методы 
    def itog(self):
        """Считает итоговую стоимость (цена * количество)."""
        return self._cena * self._kolichestvo

    def primenit_skidku(self, procent):
        """Применяет скидку к цене товара."""
        if procent < 0 or procent > 100:
            print("Ошибка: скидка должна быть от 0 до 100%.")
        else:
            self._cena = self._cena * (1 - procent / 100)
            print(f"Скидка {procent}% применена. Новая цена: {round(self._cena, 2)} руб.")

    def info(self):
        """Выводит информацию о товаре."""
        print(f"Товар: {self._nazvanie} | Категория: {self._kategoriya} | Цена: {round(self._cena, 2)} руб. | Кол-во: {self._kolichestvo} шт.")
        print(f"  Итоговая стоимость: {round(self.itog(), 2)} руб.")


# ВВОД

def vvod_tovara():
    """Спрашивает данные и создает товар."""
    nazvanie = input("Название товара: ")
    kategoriya = input("Категория: ")
    try:
        cena = float(input("Цена: "))
        kolichestvo = int(input("Количество: "))
        return Product(nazvanie, kategoriya, cena, kolichestvo)
    except ValueError:
        print("Ошибка: цена должна быть числом, а количество — целым числом.")
        return None


# ВЫВОД 

def vyvod(tovary):
    """Выводит информацию обо всех товарах."""
    if not tovary:
        print("Список товаров пуст.")
        return
    print("\n--- Список товаров ---")
    for t in tovary:
        t.info()
        print("-" * 40)


# ГЛАВНАЯ ПРОГРАММА 

def main():
    tovary = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить товар")
        print("2 - Показать все товары")
        print("3 - Применить скидку к товару")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            t = vvod_tovara()
            if t:
                tovary.append(t)
                print("Товар добавлен!")

        elif vibor == "2":
            vyvod(tovary)

        elif vibor == "3":
            if not tovary:
                print("Сначала добавьте товары.")
                continue
            vyvod(tovary)
            try:
                idx = int(input("Номер товара из списка (0, 1, ...): "))
                p = float(input("Размер скидки в %: "))
                tovary[idx].primenit_skidku(p)
            except (ValueError, IndexError):
                print("Ошибка: неверный номер товара или размер скидки.")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()