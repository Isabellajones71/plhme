#Abstraction is displaying only essential information to the user and hiding
# the details from the user

class Animal():

    animal_kind = "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        return("{}SaysI am eating Chicken".format(self.name))

# Dog1=Animal("Nyme",10)
# Dog2=Animal("Mone",5)
# print(Dog1.name)
# print("The first Dog's name is ",Dog1.name)
# print(Dog1.age)
# print(Dog1.eat())
# print(Dog2.eat())