#Inheritance
#Inheritance is a mechanism in which one class acquires the property of another class
#it allows you to call methods of the superclass in your subclass.
# The primary use case of this is to extend the functionality of the inherited method.
from animal import *
class Reptile(Animal):

    def __init__(self,name,age):
        super().__init__(name,age)

    def sleep(self):
        return('zzzz I am sleeping')
    def running(self,speed):
        return("I am running in {} speed",speed)


Rept1= Reptile('Lizzard',5)
Rept2 = Reptile('Mosy',8)
print(Rept1.eat())
