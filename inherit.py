class Calculation1:  
    def Summation(s,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(s,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(s,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  
