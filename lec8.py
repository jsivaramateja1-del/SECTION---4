'''
# print(type(3+4i)) # (This will give an error because 'i' is not defined in Python. In Python, we use 'j' to represent the imaginary part of a complex number.)
# class complex as we have noticed there is nothing defined for complex numbers
class complex:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def details(self):
        return f"x : {self.x} and y : {self.y}"
    
    def scale(self,value):
        self.x = value * self.x
        self.y = value * self.y
    
    def magnitude(self):
        return (self.x*self.x+self.y*self.y)**(0.5)
    
    def add_complex(self,other_object): # other_object carries the reference of c2
        c4 = complex(0,0)
        c4.x = self.x + other_object.x # self carries the reference of c1
        c4.y = self.y + other_object.y
        return c4
    
    def subtract_complex(self,other_object): # other_object carries the reference of c2
        c4 = complex(0,0)
        c4.x = self.x - other_object.x # self carries the reference of c1
        c4.y = self.y - other_object.y
        return c4
    
    def multiply_complex(self,other_object): # other_object carries the reference of c2
        c4 = complex(0,0)
        c4.x = (self.x * other_object.x) - (self.y * other_object.y) # self carries the reference of c1
        c4.y = (self.x * other_object.y) + (self.y * other_object.x)
        return c4
        
c1 = complex(2,3)
c2 = complex(1,2)
print(c2.details())

c3 = c1.add_complex(c2) # return c4 is stored here
print(c3.details())
print(c2.details()) 

c5 = c1.subtract_complex(c2) 
print(c5.details()) 
print(c2.details())

c6 = c1.multiply_complex(c2) # return c4 is stored here c3 = c1*c2
print(c6.details())
print(c2.details())
print(type(c1))

# c1 = complex(2,3)
# print(c1.details()) # x : 2 and y : 3
# print(f"Magnitude of c1 = {c1.magnitude():.4f}") # Magnitude of c1 = 3.6056
# c1.scale(2)
# print(c1.details()) # x : 4 and y : 6
# print(f"Magnitude of c1 = {c1.magnitude():.4f}") # Magnitude of c1 = 7.2111
'''

class person:
    
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.count = 0
        
    def __str__(self):
        return f"Name : {self.name} \nAge : {self.age} \nGender : {self.gender} \nHeight : {self.height}"
    
    def update(self, age=None, height=None):
        if age is not None:
            self.age = age
        if height is not None:
            self.height = height
    
s1 = person("abc",19,"M",160)
print(s1,"\n")
s1.update(height = 163)
s1.update(age = 23)
print(s1,"\n")

s2 = person("xyz",20,"M",170)
print(s2,"\n")
s2.update(height = 180 , age = 25)
print(s1)