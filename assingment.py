# Create a Python program that demonstrates inheritance, polymorphism, and the use of global, module, object, and local variables using real-world classes.
# Instructions:
# Inheritance and Polymorphism:
# Create a base class Vehicle with a method start_engine that prints "Engine started."
# Create a derived class Car that inherits from Vehicle and overrides the start_engine method to print "Car engine started."
# Create another derived class Bike that inherits from Vehicle and overrides the start_engine method to print "Bike engine started."
# Global Variable:
# Define a global variable traffic_light with the value "Green".
# Module Variable:
# Define a module-level variable speed_limit with the value 60.
# Object Variable:
# In the Car class, define an object variable make that stores the make of the car.
# In the Bike class, define an object variable type that stores the type of bike.
# Local Variable:
# In each start_engine method, define a local variable message that stores the respective message to be printed.

#------------------------------------------------------------------------------------------------------------------------------------------------


Traffic_Light = "Green"

Speed_Limit = 60

class Vehicle:
    def Start_Engine(self):
        message = "Engine Started"
        print(message)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make

    def Start_Engine(self):
        message = "Car Engine Started"
        print(message)

class Bike(Vehicle):
    def __init__(self, type):
        self.type = type

    def Start_Engine(self):
        message = "Bike Engine Started"
        print(message)

def main():
    car = Car("Bugatti")
    bike = Bike("Royal Enfield Himalaya")

    print("Traffic light - ", Traffic_Light)
    print("Speed limit - ", Speed_Limit)

    car.Start_Engine()
    bike.Start_Engine()

if __name__ == "__main__":
    main()
