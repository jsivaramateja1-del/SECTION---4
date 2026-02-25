class person:
    
    def __init__(self,name,age,gender,height):
        self.__name = name # private attributes
        self.__age = age # private attributes
        self.__gender = gender # private attributes
        self.__height = height # private attributes
        self.__count = 0 # private attributes
        
    def __str__(self):
        return f"Name : {self.__name} \nAge : {self.__age} \nGender : {self.__gender} \nHeight : {self.__height}"
    
    def update(self, age=None, height=None):
        if age is not None:
            self.__age = age
        if height is not None:
            self.__height = height
    
s1 = person("abc",19,"M",160)
print(s1,"\n")
# s1.__name = "acbde" # we want the details of attributes to be changed by the class. Main function does'nt have the right to change
# s1.__age = 30 
s1.update(age = 30)
s1.height(height)
print(s1,"\n")