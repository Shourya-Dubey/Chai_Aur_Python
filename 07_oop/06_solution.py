class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("Toyota", "Corolla")
safari = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(Car.total_car)