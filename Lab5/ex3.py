class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The mileage of the {self.year} {self.make} {self.model} is {self.mileage} miles per gallon."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The mileage of the {self.year} {self.make} {self.model} is {self.mileage} miles per gallon."


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"The towing capacity of the {self.year} {self.make} {self.model} is {self.towing_capacity} pounds."


car = Car("Chevrolet", "Camaro", 2022, 18)
print(car.calculate_mileage())
print()

motorcycle = Motorcycle("Honda", "Motorcycle", 2020, 50)
print(motorcycle.calculate_mileage())
print()

truck = Truck("Chevrolet", "Silverado", 2021, 12000)
print(truck.calculate_towing_capacity())
