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



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"




my_car = Car("Toyota", "Corolla")
print(Car.general_description())
# print(my_car.general_description()) <-why This working with instense insted of Car means with object of Car class