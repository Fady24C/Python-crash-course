###################[ OOP in ch9 ]######################
# - OOP -> Object oriented programming
# - Object -> Instance of a class
# - Class -> Information + behaviors (prefer first leeter is capital)
# - __init__ -> use as construct, but must begin self as parameter
# - Method -> function inside class, but must begin self as parameter
# - self -> is passed automatically, so we don’t need to pass it.
# - Abstraction -> without details
###################[ App in ch9 ]######################
# 1. Example on inhertance & Polymorphism
# - Inheritance -> share same characteristics
# - super() -> special function that helps Python make connections between the parent and child class(superclass, subclass)
# - Polymorphism -> overrideing(every class have same function) - overloading(a class contians more same function )
class Car():
    """A simple model car."""
    def __init__(self, name, salary, color):
        self.name=name
        self.salary=salary
        self.color=color
        # self.year=2012 # default value
    def defination(self):
        print(f"My car is {self.name.title()}, its color is {self.color} and costs {self.salary}.")    

class Newcar(Car):
    def __init__(self, name, salary, color, battery):
        super().__init__(name, salary, color) # Inheritance 
        self.battery=battery
    
    def defination(self): # Override
        print(f"My car is {self.name.title()}, its color is {self.color} and costs {self.salary} with battery is {self.battery}-KWH")  


print(isinstance(Newcar, Car))
print(isinstance(Car, Newcar))

MyCar_1=Car("BMW", 220000, "red")
MyCar_1.defination()
print("---------------------------")
MyCar_2=Car("Scooda", 110000, "black")
MyCar_2.defination()
print("---------------------------")
MyCar_3=Newcar("BYD", 120000, "white", 40)
MyCar_3.defination()
print("---------------------------")

#-----------------------------------------------------------------#
# 2. Example on Encapsulation + inheritance
    # - Encapsulation -> Getter/setter
    # - to make the varible private -> self.__varible
    # - In inheritance -> the child don't inheritance the private
class Person():
    def __init__(self, name, age, kind):
        self.__name=name # private
        self.__age=age
        self.__kind=kind
        
    def GetName(self):
        print(self.__name)

    def SetName(self, name):
        self.__name=name

    def GetAge(self):
        print(self.__age)

    def SetAge(self, age):
        self.__age=age
    
    def GetType(self):
        print(self.__kind)

    def SetType(self, kind):
        self.__kind=kind 

    def define(self):
        return (f"Name: {self.__age}\nAge: {self.__age}\nType: {self.__kind}\n")  

class Man(Person):
    def __init__(self, name, age, kind, skills):
        super().__init__(name, age, kind)
        self.__skills=skills

    def GetSkills(self):
        print(self.__skills)

    def SetSkills(self, skills):
        self.__skills=skills

    def define(self):
        defin= super().define()
        defin+= f"Skills: {self.__skills}"            
        return defin

Per1=Person("Weal", 12, "Male")
print(Per1.define())
print("---------------------------")
Man_1=Man("Fola", 23, "Male", ["HTML", "CSS", "JS", "Pyhton"])
print(Man_1.define())

###################[ claa in ch9 ]######################
# - static variable(class variable):
    # A variable that belongs to the class itself, not to individual objects.
    # All objects share the same copy. 
    # The value should be shared between all objects

# - static method:
    # A method that does NOT use self
    # It does NOT access instance variables
    # It does NOT access class variables (directly)
    # The function logically belongs to the class
    # But does NOT need object data

# - class method -> associative with class
    # Works with the class itself
    # Has access to class variables
    # Uses cls instead of self
    # use to intialize the construct
###################[ App in ch9 ]######################
# 3. Example on static variable + static method + class method
class Pizza():
   
    counter=0; 
    def __init__(self, ingredients):
        self.ingredients=ingredients
        Pizza.counter+=1 # static variable

    def define(self):
        print(f"> {self.counter}] Ingredients of the pizza: {self.ingredients}")

    @classmethod
    def veg(cls):
        return cls(['Mushrooms', 'olives', 'onions'])
    
    @classmethod 
    def marghrita(cls):
        return cls(['Mozarella', 'saude'])

    @staticmethod
    def price(ingredients):
        print (f"Price of pizza: {len(ingredients) * 5}")         

Piz_1=Pizza.marghrita()
Piz_1.define()

Piz_2=Pizza.veg()
Piz_2.define()

Piz_3=Pizza(["Apple", "Onions", "Tomates", "Potates"])
Piz_3.define()

Pizza.price(["one", "Two", "Three"])

# ----------[importance class method]----------------
class Student:
    school_name = "Cairo University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

###################[ claa in ch9 ]######################
# - abstract method:
    # An abstract class is a class that:
    # Cannot be instantiated directly.
    # Can contain abstract methods (methods without implementation).
    # Forces child classes to implement certain methods.

###################[ App in ch9 ]######################
from abc import ABC, abstractmethod 
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side=side   
    
    def area(self):
        return self.side*self.side
    
    
    def perimeter(self):
        return self.side*4

Sq_1 = Square(2)
print ("Area: "+ str(Sq_1.area()))
print ("perimeter: "+str(Sq_1.perimeter()))

###################[ claa in ch9 ]######################
# - Operation between objects
###################[ App in ch9 ]######################
class Math():
    def __init__(self, x):
        self.x=x
    def __add__(self, other):
        return self.x+ other.x    
    
    def __lt__(self, other):
        return self.x > other.x    
M1=Math(2)    
M2=Math(6) 
print(M1+M2)   
print(M1>M2)   
