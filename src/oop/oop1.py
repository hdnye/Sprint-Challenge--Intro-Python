# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Classes

class Vehicle:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

# Child Classes

class FlightVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return self.name

class GroundVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return self.name
 
# Granchildren Classes


class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)

class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)


class Car(GroundVehicle):
     def __repr__(self):
        return self.name

class Motorcycle(GroundVehicle):
     def __repr__(self):
        return self.name
