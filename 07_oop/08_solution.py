class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model



my_car = Car("Toyota", "Corolla")
print(my_car.model)
print(my_car.fullName())

my_car.model = "Fortuner"
print(my_car.fullName)

