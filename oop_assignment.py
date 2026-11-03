# Name: Aditya S
# Reg No: 26BCE1608
# Assessment 5: Python OOP Concepts


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Encapsulation: hiding the availability status
        self.__is_available = True

    def rent(self):
        if self.__is_available:
            self.__is_available = False
            return f"{self.brand} {self.model} is now rented."
        return f"Sorry, {self.brand} {self.model} is unavailable."

    def start_engine(self):
        # To be overridden (Polymorphism)
        pass


# Inheritance: Motorcycle inherits from Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        return f"Starting the {self.brand} {self.model} engine... Thump thump!"


# Inheritance: Car inherits from Vehicle
class Car(Vehicle):
    def start_engine(self):
        return f"Push-button start for the {self.brand} {self.model}... Purr!"


# Implementation
if __name__ == "__main__":
    my_bike = Motorcycle("Royal Enfield", "Hunter 350")
    my_car = Car("Hyundai", "i20 N Line")

    print(my_bike.start_engine())
    print(my_bike.rent())
    print(my_car.start_engine())
