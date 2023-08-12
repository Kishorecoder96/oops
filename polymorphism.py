class add:
    def __init(self,a,b,):
        a=int(input("salary"))
        b=int(input("bous"))
        
    
class salary(add):
    def __init__(self,salary,aftertax):
        self.salary=salary
        self.aftertax=aftertax
        super().__init__(a,b)
        print("salary",a+b)
        print("aftertax",a+b)
a=add()
b=salary(15000,12000)
