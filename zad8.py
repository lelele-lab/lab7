class Employee:
    """Класс, описывающий сотрудника."""

    def __init__(self, fio, dolzhnost, oklad, stazh):
        """Конструктор с защитой данных (инкапсуляция)."""
        self._fio = fio
        self._dolzhnost = dolzhnost
        
        # Защита: оклад и стаж не могут быть отрицательными
        if oklad < 0:
            print("Оклад не может быть отрицательным. Установлен 0.")
            self._oklad = 0.0
        else:
            self._oklad = oklad

        if stazh < 0:
            print("Стаж не может быть отрицательным. Установлен 0.")
            self._stazh = 0
        else:
            self._stazh = stazh

    # Свойства (геттеры)
    @property
    def fio(self):
        return self._fio

    @property
    def dolzhnost(self):
        return self._dolzhnost

    @property
    def oklad(self):
        return self._oklad

    @property
    def stazh(self):
        return self._stazh

    # Методы 
    def premiya(self):
        """Считает премию: 10% от оклада за каждый год стажа (но не более 50%)."""
        procent = self._stazh * 10
        if procent > 50:
            procent = 50  # Ограничиваем максимальную премию 50%
        
        return self._oklad * (procent / 100)

    def nalog(self):
        """Считает налог (НДФЛ 13%) с учетом оклада и премии."""
        # Налог берется с общей суммы (оклад + премия)
        obshaya_summa = self._oklad + self.premiya()
        return obshaya_summa * 0.13

    def na_ruki(self):
        """Считает сумму к выплате (оклад + премия - налог)."""
        return self._oklad + self.premiya() - self.nalog()

    def info(self):
        """Выводит информацию о сотруднике."""
        print(f"Сотрудник: {self._fio} | Должность: {self._dolzhnost}")
        print(f"  Оклад: {self._oklad} руб. | Стаж: {self._stazh} лет")
        print(f"  Премия: {round(self.premiya(), 2)} руб.")
        print(f"  Налог (13%): {round(self.nalog(), 2)} руб.")
        print(f"  К выплате: {round(self.na_ruki(), 2)} руб.")


# ВВОД 

def vvod_sotrudnika():
    """Спрашивает данные и создает сотрудника."""
    fio = input("Введите ФИО: ")
    dolzhnost = input("Введите должность: ")
    try:
        oklad = float(input("Введите оклад: "))
        stazh = int(input("Введите стаж (лет): "))
        return Employee(fio, dolzhnost, oklad, stazh)
    except ValueError:
        print("Ошибка: оклад должен быть числом, а стаж — целым числом.")
        return None


# ВЫВОД

def vyvod(sotrudniki):
    """Выводит информацию обо всех сотрудниках."""
    if not sotrudniki:
        print("Список сотрудников пуст.")
        return
    print("\n--- Список сотрудников ---")
    for s in sotrudniki:
        s.info()
        print("-" * 40)


# ГЛАВНАЯ ПРОГРАММА

def main():
    sotrudniki = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить сотрудника")
        print("2 - Показать всех сотрудников")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            s = vvod_sotrudnika()
            if s:
                sotrudniki.append(s)
                print("Сотрудник добавлен!")

        elif vibor == "2":
            vyvod(sotrudniki)

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()