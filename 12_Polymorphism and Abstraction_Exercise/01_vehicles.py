from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, drive):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def drive(self, distance):
        consume = (Car.AIR_CONDITIONER + self.fuel_consumption) * distance

        if self.fuel_quantity >= consume:
            self.fuel_quantity -= consume

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6
    TANK = 0.95

    def drive(self, distance):
        consume = (Truck.AIR_CONDITIONER + self.fuel_consumption) * distance

        if self.fuel_quantity >= consume:
            self.fuel_quantity -= consume

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TANK


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

