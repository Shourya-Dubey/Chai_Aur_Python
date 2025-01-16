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
    

class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Toyta", "Corola")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
print(my_new_tesla.fullName())