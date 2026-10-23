class BankAccount:
    """Класс, описывающий банковский счет."""

    def __init__(self, nomer, vladeles, balans=0.0):
        """Конструктор с инкапсуляцией."""
        self._nomer = nomer
        self._vladeles = vladeles
        # Защита: баланс не может быть отрицательным при создании
        if balans < 0:
            print("Баланс не может быть отрицательным. Установлен 0.")
            self._balans = 0.0
        else:
            self._balans = balans

    # Свойства (геттеры)
    @property
    def nomer(self):
        return self._nomer

    @property
    def vladeles(self):
        return self._vladeles

    @property
    def balans(self):
        return self._balans

    # Методы 
    def popolnit(self, summa):
        """Пополнение баланса."""
        if summa <= 0:
            print("Сумма пополнения должна быть больше нуля.")
            return
        self._balans += summa
        print(f"Счет {self._nomer} пополнен на {summa} руб. Текущий баланс: {self._balans} руб.")

    def snyat(self, summa):
        """Снятие наличных."""
        if summa <= 0:
            print("Сумма снятия должна быть больше нуля.")
        elif summa > self._balans:
            print(f"Недостаточно средств! На счете только {self._balans} руб.")
        else:
            self._balans -= summa
            print(f"Со счета {self._nomer} снято {summa} руб. Остаток: {self._balans} руб.")

    def perevod(self, drugoy_schet, summa):
        """Перевод на другой счет."""
        if summa <= 0:
            print("Сумма перевода должна быть больше нуля.")
        elif summa > self._balans:
            print(f"Недостаточно средств для перевода! На счете только {self._balans} руб.")
        else:
            # Снимаем у себя и добавляем получателю
            self._balans -= summa
            drugoy_schet._balans += summa
            print(f"Перевод {summa} руб. со счета {self._nomer} на счет {drugoy_schet.nomer} выполнен успешно.")

    def info(self):
        """Выводит информацию о счете."""
        print(f"Счет: {self._nomer} | Владелец: {self._vladeles} | Баланс: {self._balans} руб.")


# ВВОД 

def vvod_scheta():
    """Спрашивает данные и создает счет."""
    nomer = input("Введите номер счета: ")
    vladeles = input("Введите ФИО владельца: ")
    try:
        balans = float(input("Начальный баланс (можно 0): "))
        return BankAccount(nomer, vladeles, balans)
    except ValueError:
        print("Ошибка: баланс должен быть числом.")
        return None


# ВЫВОД 

def vyvod(scheta):
    """Выводит информацию обо всех счетах."""
    if not scheta:
        print("Счетов пока нет.")
        return
    print("\n--- Список счетов ---")
    for s in scheta:
        s.info()


# ГЛАВНАЯ ПРОГРАММА

def main():
    scheta = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Открыть новый счет")
        print("2 - Показать все счета")
        print("3 - Пополнить счет")
        print("4 - Снять деньги")
        print("5 - Перевести деньги")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            acc = vvod_scheta()
            if acc:
                scheta.append(acc)
                print("Счет открыт!")

        elif vibor == "2":
            vyvod(scheta)

        elif vibor == "3":
            vyvod(scheta)
            try:
                idx = int(input("Номер счета из списка (0, 1, ...): "))
                summa = float(input("Сумма пополнения: "))
                scheta[idx].popolnit(summa)
            except (ValueError, IndexError):
                print("Ошибка: неверные данные или номер счета.")

        elif vibor == "4":
            vyvod(scheta)
            try:
                idx = int(input("Номер счета из списка: "))
                summa = float(input("Сумма снятия: "))
                scheta[idx].snyat(summa)
            except (ValueError, IndexError):
                print("Ошибка: неверные данные или номер счета.")

        elif vibor == "5":
            vyvod(scheta)
            if len(scheta) < 2:
                print("Для перевода нужно минимум 2 счета.")
                continue
            try:
                idx_from = int(input("С какого счета (номер): "))
                idx_to = int(input("На какой счет (номер): "))
                summa = float(input("Сумма перевода: "))
                if idx_from == idx_to:
                    print("Нельзя перевести деньги на тот же счет.")
                else:
                    scheta[idx_from].perevod(scheta[idx_to], summa)
            except (ValueError, IndexError):
                print("Ошибка: неверные данные или номер счета.")

        elif vibor == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()