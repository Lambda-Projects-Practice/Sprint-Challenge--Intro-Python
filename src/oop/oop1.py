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

class Vehicle:
    #base class
    pass

class GroundVehicle(Vehicle):
    #inherits from vehicle
    pass

class Car(GroundVehicle):
    #inherits from groundvehicle which inherits from vehicle
    pass

class Motorcycle(GroundVehicle):
    #inherits from groundvehicle which inherits from vehicle
    pass

class FlightVehicle(Vehicle):
    #inherits from vehicle
    pass

class Starship(FlightVehicle):
    #inherits from flightvehicle which inherits from vehicle
    pass

class Airplane(FlightVehicle):
    #inherits from flightvehicle which inherits from vehicle
    pass