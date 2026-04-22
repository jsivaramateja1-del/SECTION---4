'''
class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("Cat Meows")
        
class animal(Dog,Cat):
    def sound(self):
        print("Animal makes sound")

animal_1 = animal()
animal_1.sound()
'''

'''
l = [1,2,4,4,"jodwuf"]
t = (1,6,9,66)
dc = {"a" : 5 , "b" : 6}
s = "abcde"
s1 = {1,3,5,5}
print(len(l))
print(len(t))
print(len(dc))
print(len(s))
print(len(s1))
'''

'''
def add(a,b):
    return a+b
    
# static binding
print(add(23,4))

def add(a,b,c):
    return a+b+c

print(add(2,4,5))
'''
'''
# dynamic binding
class Animal:
    def sound(self):
        print("Animal makes sound !")
    # pass
    
class Dog(Animal):
    def sound(self):
        print("Dog Barks !")
    # pass

animal = Animal()
animal.sound()
dog = Dog()
dog.sound()
'''

'''
class animal:
    def speak(self):
        print("Animal makes sound")
        
class dog(animal):
    def speak(self):
        print("Dog barks")
    # pass

class cat(animal):
    # def speak(self):
    #     print("Cat meows !")
    pass
        
def animal_sound(animals): # function to call out for methods in classes
    animals.speak()
d1 = dog()
c1 = cat()
animal_sound(d1)
animal_sound(c1)
'''

import numpy as np  

a = np.linspace(1,10,5)
print(a)