'''
class employee:
    def __init__(self,name,Id,salary):
        self.name = name
        self.Id = Id
        self.salary = salary
        
    def __str__(self):
        return f"Name : {self.name} \nId : {self.Id} \nSalary : {self.salary}"
    
    def update(self,value):
        self.salary = value
        return f"Your Salary has been updated to {self.salary}"
    
class sde(employee):
    def __init__(self, name, Id, salary,role):
        super().__init__(name, Id, salary)
        self.role = role
    
    def __str__(self):
        # print(super().__str__()) #  this is calling method from parent class
        # return f"role : {self.role}"
        return super().__str__() + f"\nrole : {self.role}"
    
class senior_sde(sde):
    def __init__(self,name,Id,salary,role,level):
        super().__init__(name,Id,salary,role)
        self.level = level
        
    def __str__(self):
        # print(super().__str__()) #  this is calling method from parent class
        # return f"level : {self.level}"
        return super().__str__() + f"\nlevel : {self.level}"
        
sn1 = senior_sde("xyz",13,100000,"sde","1")
print(sn1)
'''
'''
class A:
    def details1(self):
        print("Class A")

class B:
    def details2(self):
        print("Class B")
        
class C(A,B):
    def details3(self):
        super().details1()
        super().details2()
        # print("Class C")
    # pass

c = C()
c.details3()
# c.details2()
'''

class A:
    def __init__(self):
        super().__init__()
        print("Class A")
        
class B:
    def __init__(self):
        super().__init__()
        print("Class B")
        
class D:
    def __init__(self):
        super().__init__()
        print("Class D")
        
class C(A,B,D):
    def __init__(self):
        super().__init__()
        # A.__init__(self)
        # B.__init__(self)
        # D.__init__(self)
        print("Class C")

print(C.__mro__)  # prints order of calling class method
c = C()