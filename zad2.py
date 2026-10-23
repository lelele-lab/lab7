class Student:
    """Класс, описывающий студента."""

    def __init__(self, fio, gruppa, ocenki):
        """Конструктор с защитой данных."""
        self._fio = fio
        self._gruppa = gruppa
        # Оценки передаем списком (например, [5, 4, 2, 3])
        self._ocenki = ocenki

    # Свойства (геттеры)
    @property
    def fio(self):
        return self._fio

    @property
    def gruppa(self):
        return self._gruppa

    @property
    def ocenki(self):
        return self._ocenki

    # Методы (вычисления) 
    def sredniy_ball(self):
        """Считает средний балл."""
        if not self._ocenki:
            return 0.0
        return sum(self._ocenki) / len(self._ocenki)

    def dolgi(self):
        """Возвращает список предметов (индексов оценок), где стоят двойки."""
        # оценки, считаем по индексам
        dolgi_list = []
        for i in range(len(self._ocenki)):
            if self._ocenki[i] == 2:
                # i+1, чтобы для пользователя предметы считались с 1, а не с 0
                dolgi_list.append(i + 1) 
        return dolgi_list

    def info(self):
        """Выводит информацию о студенте."""
        print(f"Студент: {self._fio} | Группа: {self._gruppa} | Оценки: {self._ocenki}")


# ВВОД 

def vvod_studenta():
    """Спрашивает данные и создает объект Student."""
    fio = input("Введите ФИО: ")
    gruppa = input("Введите группу: ")
    
    print("Введите оценки через пробел (например, 5 4 3 2):")
    ocenki_str = input().split()
    
    # Превращаем строки в числа
    ocenki = []
    for o in ocenki_str:
        try:
            ocenki.append(int(o))
        except ValueError:
            print("Ошибка: введено не число. Эта оценка пропущена.")

    return Student(fio, gruppa, ocenki)


#  ВЫВОД 

def vyvod(studenty):
    """Выводит информацию обо всех студентах."""
    print("\n--- Список студентов ---")
    for s in studenty:
        s.info()
        print(f"Средний балл: {round(s.sredniy_ball(), 2)}")
        
        dolgi = s.dolgi()
        if dolgi:
            print(f"Долги по предметам №: {dolgi}")
        else:
            print("Долгов нет.")
        print("-" * 30)


# ГЛАВНАЯ ПРОГРАММА 

def main():
    studenty = []

    while True:
        print("\n1 - Добавить студента")
        print("2 - Показать всех студентов и их успеваемость")
        print("0 - Выход")
        vibor = input("Выбор: ")

        if vibor == "1":
            studenty.append(vvod_studenta())
            print("Студент добавлен!")
        elif vibor == "2":
            if not studenty:
                print("Список пуст.")
            else:
                vyvod(studenty)
        elif vibor == "0":
            break
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()