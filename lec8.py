'''
print(type(5))
print(type(5.0))
print(type('5'))
print(type(True))
print(type(2+5j))
'''
'''
S = "Sai"
S1 = "Uni"
S2 = S + S1
#S3 = S - S1 #(Not defined for strings)
print(S2)
#print(S3)
#S4 = S % S1 #(Not defined for strings, but we can use % operator for string formatting)
#print(S4)
# S5 = S * S1 #(Not defined for strings, but we can multiply a string with an integer)
# print(S5)
'''
'''
# cylinder
class cylinder:
    def __init__(self,h,r): # constructor #initilize the object
        self.h = h # attributes or data members
        self.r = r 
    def volume(self): # member function or methods
        return 3.14*self.r*self.r*self.h
    def surface_area(self):
        return 2*3.14*self.r*self.h
    
c1 = cylinder(1,1)
c2 = cylinder(2,3)
print("Volume of cylinder is : ",c1.volume())
print("Surface area of cylinder is :",c1.surface_area())
print("Volume of cylinder is : ",c2.volume())
print("Surface area of cylinder is :",c2.surface_area())
'''
class person:
    
    def __init__(self,name,id,cgpa): # constructor
        self.name = name
        self.id = id
        self.cgpa = cgpa
        
    def details(self): # method
        return f"Name : {self.name}\nID : {self.id}\nCGPA : {self.cgpa}"
    
    def cgpa_checker(self):
        if self.cgpa >= 8:
            return "Keep It Up"
        else:
            return "You can do better"
        
    def update_cgpa(self):
        new_cgpa = float(input("Enter new CGPA : "))
        self.cgpa = new_cgpa
        return self.cgpa
    
p1 = person("AUDI",18,9.4)
print(p1.details())
print(p1.cgpa_checker())
print(p1.update_cgpa())
print(p1.cgpa_checker())
print()

p2 = person("HARSHA",19,9.5)
print(p2.details())
print(p2.cgpa_checker())
print(p2.update_cgpa())
print(p2.cgpa_checker())
print()

p3 = person("Teja",15,7.6)
print(p3.details())
print(p3.cgpa_checker())
print(p3.update_cgpa())
print(p3.cgpa_checker())
