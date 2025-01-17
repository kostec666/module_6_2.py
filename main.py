class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Список допустимых цветов

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 4 # Ограничение на количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Пример использования
vehicle1 = Sedan('Fedos', 'Dodge chalenger', 'blue', 10000)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Red')  # Этот цвет не допустим
vehicle1.set_color('White')  # Этот цвет допустим
vehicle1.owner = 'Kostec'  # Меняем владельца

# Проверяем что поменялось
vehicle1.print_info()


