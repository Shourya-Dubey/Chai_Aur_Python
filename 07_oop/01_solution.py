class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesl"
    
    @staticmethod
    def general_description():
        return "Cars are menas of transport"
    
    @property
    def model(self):
        return self.__model
    

        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"




# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fullName())
# print(my_tesla.fuel_type())
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

safari = Car("Tata", "Safari")
# safari.model = "City"
# print(safari.model)
# print(safari.fuel_type())
# print(Car.total_car)
# print(safari.general_description())
# print(Car.general_description())


class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())