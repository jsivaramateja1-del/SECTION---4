# Revison Object Oriented Programming
'''
class complex:
    def __init__(self,x,y): # self carries the address of each object created using this class
        self.x = x
        self.y = y
    
    def get_details(self): # method
        return f"{self.x} + {self.y}i"
    
    def add(self,other_object): # other object carries the reference of second object
        self.x = self.x + other_object.x
        self.y = self.y + other_object.y
        return self
    
    def multiply(self,other_object):
        c4 = complex(0,0)
        c4.x = (self.x * other_object.x) - (self.y * other_object.y) # self carries the reference of c1
        c4.y = (self.x * other_object.y) + (self.y * other_object.x)
        return c4
    
c1 = complex(1,2)
c2 = complex(3,4)
print(c1.get_details())
c3 = c1.add(c2) 
print(c3.get_details()) 
c4 = c1.multiply(c2)
print(c4.get_details())
'''

class person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}\nHeight : {self.height}"
    
    def update(self,age = None,height = None):
        if age is not None:
            self.age = age
        if height is not None:
            self.height = height
            
class employee(person):
    def __init__(self,name,age,height,role):
        super().__init__(name,age,height) # it initializing the things that are there in class person
        self.role = role
    
    def get_details(self):
        print(e1.role)
        print(self)
        
e1 = employee("abc",24,170,"data analyst")
print(e1)
e1.update(age = 30)
e1.get_details()


'''
class animal: # Parent class
    def sound(self):
        return "some kind of sound"
    
    def move(self):
        return "animal moves"
    
class dog(animal): # Child class
    def dogs_sound(self):
        return "Dog barks"
    
    def dogs_move(self):
        return "Dog runs"
    
d1 = dog()
print(d1.sound())  # This method is being called from parent class
print(d1.dogs_sound()) # This is from child class
print(d1.move())
print(d1.dogs_move())
'''