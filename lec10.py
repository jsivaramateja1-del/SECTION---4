'''
class TermMarks:
    def __init__(self,Term1 = 0,Term2 = 0,Term3 = 0):
        self.__Term1 = Term1 
        self.__Term2 = Term2
        self.__Term3 = Term3
        if self.__Term1 < 0:
            self.__Term1 = 0
        if self.__Term2 < 0:
            self.__Term2 = 0
        if self.__Term3 < 0:
            self.__Term3 = 0
    def average(self): # average of term marks
        return f"The average of the given marks = {(self.__Term1 + self.__Term2 + self.__Term3)/3}"
    def maximum(self): # maximum of term marks
        if self.__Term1 >= self.__Term2 and self.__Term1 >= self.__Term3:
            Max = self.__Term1
        elif self.__Term2 >= self.__Term1 and self.__Term2 >= self.__Term3:
            Max = self.__Term2
        else:
            Max = self.__Term3
        return f"The maximum of the given marks = {Max}"
    def __str__(self):
        return f"Marks are\nTest 1 : {self.__Term1}\nTest 2 : {self.__Term2}\nTest 3 : {self.__Term3}"
    
t = TermMarks()
print(t)
print(t.average())
print(t.maximum())
print()

t1 = TermMarks(12,45,90)
print(t1)
print(t1.average())
print(t1.maximum())
print()

t2 = TermMarks(-1,34,35)
print(t2)
print(t2.average())
print(t2.maximum())
print()
'''

# My own list

class my_list:
    def __init__(self):
        self.l = [0,0,0,0,0,0,0,0,0,0,0]
        self.count = 0
    def my_append(self,value):
        self.l[self.count] = value
        self.count = self.count + 1
    def print_list(self):
        print("[",end="")
        for i in range(self.count):
            print(self.l[i],end = ",")
        print("]")
    def update(self,index,value):
        if index < self.count:
            self.l[index] = value
        else:
            print("Index out of range.")
    def insert(self,index,value):
        if self.count < len(self.l) and index < self.count:
            for i in range(self.count-1,index-1,-1):
                self.l[i+1] = self.l[i]
            self.l[index] = value
            self.count = self.count + 1
        else:
            print("Index out of range.")
    def delete_index(self,index):
        if index < self.count:
            for i in range(index,self.count-1):
                self.l[i] = self.l[i+1]
            self.l[self.count-1] = 0
            self.count = self.count - 1
        else:
            print("Index out of range.")
    def delete_value(self,value):
        for i in range(self.count):
            if self.l[i] == value:
                for j in range(i,self.count-1):
                    self.l[j] = self.l[j+1]
                self.l[self.count-1] = 0
                self.count = self.count - 1
                return
        print("Value not found.")
l1 = my_list()
l1.my_append(4)
l1.my_append(56)
l1.my_append(99)
l1.my_append(100)
l1.print_list()
l1.update(0,5)
l1.print_list()
l1.insert(2,900)
l1.print_list()
l1.insert(4,56)
l1.print_list()
l1.delete_index(4)
l1.print_list()
l1.delete_value(900)
l1.print_list()