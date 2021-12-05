# object oriented programming is the most important for deriving objects and classes and methods 


#Inheritance 
 #Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes.

# Base class
class Vehicle:# parent class
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):# sub class
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):# sub classs
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()# method
s_car.car_info()
s_car.sports_car_info()

# here invloves types of inheritances
# single ,multi ,multiple level,hybrid inheritance
