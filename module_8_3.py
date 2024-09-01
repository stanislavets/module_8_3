class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_number, car_numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = car_numbers
        self.__is_valid_vin(vin_number)
        self.__is_valid_numbers(car_numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber  ('Диапазон для vin номера')

    def __is_valid_numbers(self, car_numbers):
        if not isinstance(car_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(car_numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

try:
    first = Car('Model1', 1000000, 'f123dj')
    print(f'{first.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)

try:
    second = Car('Model2', 300, 'т001тр')
    print(f'{second.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)

try:
    third = Car('Model3', 2020202, 'нет номера')
    print(f'{third.model} успешно создан')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)