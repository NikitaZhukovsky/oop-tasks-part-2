class Bus:
    def __init__(self, speed, max_seats, max_speed):
        if isinstance(speed, (int, float)) and speed > 0:
            self.speed = speed
        else:
            raise ValueError("Скорость должна быть положительным числом.")

        if isinstance(max_seats, (int, float)) and max_seats > 0:
            self.max_seats = max_seats
        else:
            raise ValueError("Количество мест должно быть положительным числом.")

        if isinstance(max_speed, (int, float)) and max_speed > 0:
            self.max_speed = max_speed
        else:
            raise ValueError("Максимальная скорость должна быть положительным числом.")

        self.passenger_list = []
        self.has_free_seats = True
        self.seat_map = {}

    def embark(self, *passengers):
        if len(self.passenger_list) + len(passengers) <= self.max_seats:
            self.passenger_list.extend(passengers)
            self.has_free_seats = len(self.passenger_list) < self.max_seats
            for index, passenger in enumerate(self.passenger_list, start=1):
                self.seat_map[passenger] = index
            print("Пассажиры рассажены в автобусе")
        else:
            print("Недостаточно мест в автобусе")

    def disembark(self, *passengers):
        for passenger in passengers:
            if passenger in self.passenger_list:
                self.passenger_list.remove(passenger)
                del self.seat_map[passenger]
        self.has_free_seats = len(self.passenger_list) < self.max_seats
        print("Пассажиры высажены из автобуса")

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
            print(f"Скорость автобуса увеличена на {value}")
        else:
            print("Автобус уже достиг максимальной скорости!")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Скорость автобуса снижена на {value}")
        else:
            print("Невозможно снизить скорость, так как она будет меньше 0!")

    def __contains__(self, passenger):
        return passenger in self.passenger_list

    def __iadd__(self, passengers):
        self.embark(*passengers)
        return self

    def __isub__(self, passengers):
        self.disembark(*passengers)
        return self


def menu():
    bus = Bus(80, 30, 180)

    while True:
        print("Меню:")
        print("1. Посадка одного или нескольких пассажиров")
        print("2. Наличие свободных мест")
        print("3. Высадка пассажиров")
        print("4. Наличие пассажиров в автобусе")
        print("5. Текущая скорость автобуса")
        print("6. Увеличение скорости автобуса")
        print("7. Уменьшение скорости автобуса")
        print("8. Добавление пассажира/пассажира при помощи операции +=")
        print("9. Высадка пассажира/пассажиров при помощи операции -=")
        print("10. Выход")

        choice = int(input("Выберите действие (1-10): "))

        match choice:
            case 1:
                passenger_input = input("Введите пассажира или пассажиров (через запятую): ")
                passengers = passenger_input.split(",")
                bus.embark(*passengers)
                print("Рассадка в автобусе:", bus.seat_map)
            case 2:
                print(f"Доступны свободные места: {bus.has_free_seats}")
            case 3:
                passenger_input = input("Введите пассажира или пассажиров (через запятую): ")
                passengers = passenger_input.split(",")
                bus.disembark(*passengers)
                print("Рассадка в автобусе:", bus.seat_map)
            case 4:
                passenger = input("Введите пассажира, которого вы хотите найти в автобусе: ")
                print(f"Пассажир {passenger} в автобусе: {passenger in bus}")
            case 5:
                print(f"Текущая скорость автобуса: {bus.speed}")
            case 6:
                state = True
                while state:
                    speed = input("На сколько вы хотите увеличить скорость автобуса: ")
                    if speed.isdigit() and float(speed) > 0:
                        speed = float(speed)
                        state = False
                    else:
                        print("Ошибочный ввод, попробуйте ещё раз!")
                bus.increase_speed(speed)
            case 7:
                state = True
                while state:
                    speed = input("На сколько вы хотите увеличить скорость автобуса: ")
                    if speed.isdigit() and float(speed) > 0:
                        speed = float(speed)
                        state = False
                    else:
                        print("Ошибочный ввод, попробуйте ещё раз!")
                bus.decrease_speed(speed)
            case 8:
                passenger_input = input("Введите пассажира или пассажиров (через запятую): ")
                passengers = passenger_input.split(",")
                bus += passengers
                print("Рассадка в автобусе:", bus.seat_map)
            case 9:
                passenger_input = input("Введите пассажира или пассажиров (через запятую): ")
                passengers = passenger_input.split(",")
                bus -= passengers
                print("Рассадка в автобусе:", bus.seat_map)
            case 10:
                print("Выход из программы.")
                break
            case _:
                print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 8.")


menu()
