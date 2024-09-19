class Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __new__(cls, *args, **kwargs):
        cls.COLOR_VARIANTS.append(args[0])
        return object.__new__(cls)
    def __init__(self, owner, model, engine_power, color, COLOR_VARIANTS):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.__COLOR_VARIANTS = COLOR_VARIANTS
    def get_model(self, model):
        return f'Модель: {self.__model}'
    def get_horsepower(self, engine_power):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self, color):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(f'{self.__model}, {self.__engine_power}, {self.__color}, Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color, COLOR_VARIANTS, PASSENGER_LIMIT):
        super().__init__(owner, model, engine_power, color, COLOR_VARIANTS)
        self.__PASSENGER_LIMIT = PASSENGER_LIMIT

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()




    
