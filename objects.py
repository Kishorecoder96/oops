class company:
    def __init__(self,laptop,employee,salary) -> None:
        self.laptop=laptop
        self.employee=employee
        self.salary=salary

    def display(self):
        print("LAPTOP:",self.laptop)
        print("EMPLOYEE:",self.employee)
        print("SALARY",self.salary)

class patients:
    def __init__(self,name,age,disease,doctor):
        self.name=name
        self.age=age
        self.disease=disease
        self.doctor=doctor
    def display1(self):
        print("PATIENT NAME:",self.name)
        print("AGE:",self.age)
        print("DISEASE:",self.disease)
        print("DOCTOR:",self.doctor)
a=company("hp","akilesh","60000")
a.display()
b=patients("HARISHVAR","21","BLINDNESS","KANNAL",)
b.display1()

