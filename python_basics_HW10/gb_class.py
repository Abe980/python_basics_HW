class Tyre:
    def __init__(self, weather: str, brand: str):
        self.weather = weather
        self.brand = brand

    def __str__(self):
        return f'{"Летняя" if self.weather == "summer" else "Зимняя"} резина марки {self.brand}'


class Wheel:
    def __init__(self, size: int, brand: str, weather: str, brand_t: str = ''):
        self.size = size
        self.brand = brand

        self.tyre = Tyre(weather, brand_t if brand_t else brand)


class Car:
    def __init__(self, mark: str, color: str, year: int, size_w: int = 17, brand_w: str = 'Firestone'):
        self.mark = mark
        self.color = color
        self.year = year
        self.wheels = [Wheel(size_w, brand_w, 'summer'),
                       Wheel(size_w, brand_w, 'summer'),
                       Wheel(size_w, brand_w, 'summer'),
                       Wheel(size_w, brand_w, 'winter')]

    def __str__(self):
        return f'Машина марки {self.mark}, цвет: {self.color}, год выпуска {self.year}'

    def horn(self):
        print(f'Машина {self.mark} делает "би-би-биииииии"')


my_car = Car('Mazda', 'black', 2019)
new_car = Car('Tesla', 'white', 2023, 20, 'Белшина')

my_car.horn()
new_car.horn()

print(my_car.mark)
print(new_car.mark)

my_car.wheels[1].brand = 'Запаска'
my_car.wheels[1].size = 14

for wheel in my_car.wheels:
    print(wheel.size, wheel.brand, wheel.tyre)

print(my_car)
