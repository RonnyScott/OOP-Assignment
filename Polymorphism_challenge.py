class Vehicle:
    def move(self):
        """General move method for a vehicle"""
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return "Driving "


class Plane(Vehicle):
    def move(self):
        return "Flying "


class Boat(Vehicle):
    def move(self):
        return "Sailing "



vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())

