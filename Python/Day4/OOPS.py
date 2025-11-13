#Made By Punit

=================== x x x x x x x x ===================

#Question

#Create class named as Rectangle.
#There is attributes in it length and width.
#these is method named as area which return area of rectangle.
#Get input from user for a and b.

#hint:
#area=lenght*breadth
#return area

#l=float(input("Enter lenght:"))
#w=float(input("Enter width:"))

#area=Rectangle(l,w)

=================== x x x x x x x x ===================

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

rect = Rectangle(l, w)

print("Area of Rectangle:", rect.area())

=================== x x x x x x x x ===================

#Class

=================== x x x x x x x x ===================

class Car:
  def __init__(self,brand,color):
    self.brand=brand #attribute
    self.color=color #attribute

   def drive(self): #method
     print(f"I am Driving {self.color} {self.brand}.")

#Object

car1= Car("Lord Alto","Modified")
car2= Car("Nano","Yellow")

car1.drive()
car2.drive()

=================== x x x x x x x x ===================

#OOPS : There are 4 Pillors in Oops

=================== x x x x x x x x ===================

#Encapsulation --> binding data + methods together

=================== x x x x x x x x ===================

#Bank Account

class BankAccount:
  def __init__(self,balance):
    self.__balance += balance

   
  def deposit(self,amount):
    self.__amount +=amount

  def get_balance(self):
    return self.__balance 

account = BankAccount(1000)
account.deposit(500)
print(account.get__balance()) #1500

=================== x x x x x x x x ===================

#Inheritance

=================== x x x x x x x x ===================

#Class Car

class car:
  def __init__(self,brand,color):
    self.brand=brand #attribute
    self.__color=color #attribute for private some details

  def drive(self): #mentioned
    print(f"{self.__color} {self.brand}is driving 🚗")

#Object

car1=car("Tesla","black")
car2=car("Verna","white")

print(car1.brand)
print(car1.__color) #It shows error
print(car2.brand)
print(car2.__color)
print(car2.__car__color) #To get private value

car1.drive()
car2.drive()

=================== x x x x x x x x ===================

#Polymorphism : Same Funtion Different Value

=================== x x x x x x x x ===================

#Class Animal 

class animal:
  def name(self):
    print("animal speaks")

class Dog(animal):
  def name(self):
    print("dog barks🐶")

dog=Dog()
dog.speak()  

=================== x x x x x x x x ===================

class Friend:
  def sound(self):
    return "Yash"
    
class Mine:
  def sound(self):
    return "Punit"

for a in [Friend(),Mine()]:
  print(a.Mine())
  print(a.Friend())

=================== x x x x x x x x ===================
   
class Animal:
  def speak(self):
    print("Animal make different sound")

class Dog(Animal):
  def speak(self):
    print("Dog barks")

class Cat(Animal):
  def speak(self):
    print("Cat meows")

for pet in (Dog(),Cat()):
    pet.speak()

=================== x x x x x x x x ===================

#Abstraction

=================== x x x x x x x x ===================

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print("Car started")

class Bike(vehicle):
    def start(self):
        print("Bike started")

vehicles = [Car(),Bike()]

for v in vehicles:
    v.start()


=================== x x x x x x x x ===================


#Made By Punit
