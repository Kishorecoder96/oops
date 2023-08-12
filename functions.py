def func(self,a,b):
    a="roe"
    b="john"
    print(a+b)

def func1(self,a,b):
    a=int(input())
    b=int(input())
    print(a-b)

class insurance:
    def __init__(self,name,policyname,details):
        self.name=input()
        self.policyname=input()
        self.details=input()
        print(self.name ,self.policyname , details) 

func("vinay","mohan","ram")
func1(18,20,30)
c=insurance("KISHORE","IOS MAMA","13000 PER YEAR")