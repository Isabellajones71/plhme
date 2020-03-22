#Encapsulation
#In an object oriented python program, you can restrict access to methods and variables.
#This can prevent the data from being modified by accident and is known as encapsulation
from reptile import *
class Snake(Reptile):


    def __init__(self, name, age):
        super().__init__(name, age)

        self.name = name
        self.age = age
    def seek_heat(self):
        return("Let me see some sunshine")
    def sleep(self):
        return("Please leave me to sleep")

Sidney = Snake("DOO",2)
print(Sidney.eat())
print(Sidney.sleep())

#Polymorphism-Polymorphism in python defines methods in the child class that have the same
# name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class.
# Also, it is possible to modify a method in a child class
# that it has inherited from the parent class and this is called as method overriding
