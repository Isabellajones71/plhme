#In an object oriented python program, you can restrict access to methods and variables.
# This can prevent the data from being modified by accident and is known as encapsulation.
class Car:


    def __init__(self):
        self.__maxspeed = 200
        self.name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.maxspeed = speed


redcar = Car()
redcar.drive()
redcar.setMaxSpeed(450)
redcar.drive()