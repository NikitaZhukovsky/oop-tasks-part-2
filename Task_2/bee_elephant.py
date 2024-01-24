class BeeElephant:
    def __init__(self, bee, elephant):
        if isinstance(bee, (int, float)) and bee > 0:
            self.bee = bee
        else:
            raise ValueError("Ошибка ввода!")

        if isinstance(elephant, (int, float)) and elephant > 0:
            self.elephant = elephant
        else:
            raise ValueError("Ошибка ввода!")


    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.bee += value
            self.elephant -= value
        elif meal == "grass":
            self.bee -= value
            self.elephant += value

        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0

        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0


# Создание экземпляра класса
bee_elephant = BeeElephant(80, 30)

print(f"Часть пчелы не меньше части слона: {bee_elephant.fly()}")
print(f"Часть слона не меньше части пчелы: {bee_elephant.trumpet()}")

state = True
while state:
    input_meal = input('Введите еду (grass or nectar): ')
    if input_meal == "grass" or input_meal == "nectar":
        state = False
    else:
        print("Неправильный ввод, попробуйте ещё раз!")

state = True
while state:
    input_value = input("Введите сколько вы хотите съесть (целое число): ")
    if input_value.isdigit() and int(input_value) > 0:
        input_value = int(input_value)
        state = False
    else:
        print("Ощибка ввода, попрбуйте ещё раз!")

bee_elephant.eat(input_meal, input_value)
print(f"Часть пчелы не меньше части слона: {bee_elephant.fly()}")
print(f"Часть слона не меньше части пчелы: {bee_elephant.trumpet()}")

state = True
while state:
    input_meal = input('Введите еду: ')
    if input_meal == "grass" or input_meal == "nectar":
        state = False
    else:
        print("Неправильный ввод, попробуйте ещё раз!")

state = True
while state:
    input_value = input("Введите сколько вы хотите съесть (целое число): ")
    if input_value.isdigit() and int(input_value) > 0:
        input_value = int(input_value)
        state = False
    else:
        print("Ощибка ввода, попрбуйте ещё раз!")

bee_elephant.eat(input_meal, input_value)
print(f"Часть пчелы не меньше части слона: {bee_elephant.fly()}")
print(f"Часть слона не меньше части пчелы: {bee_elephant.trumpet()}")
