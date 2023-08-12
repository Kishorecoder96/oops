class princ:
    def __init__(self,name,principal,circular) -> None:
        self.name=name
        self.position=principal
        self.circular=circular
    def msg(self,name,principal,circular):
        print(self.name)
        print(self.position)
        print(self.circular)

class teacher(princ):
    def __init__(self,name,principal,circular) -> None:
        self.name=name
        self.position=principal
        self.circular=circular
        print(self.name)
        print(self.position)
        print(self.circular)

class student(teacher):
    def __init__(self,name,principal,circular) -> None:
        self.name=name
        self.position=principal
        self.circular=circular
        print(self.name)
        print(self.position)
        print(self.circular)

class parents(student):
    def __init__(self,name,principal,circular) -> None:
        self.name=name
        self.position=principal
        self.circular=circular
        print(self.name)
        print(self.position)
        print(self.circular)
a=princ("MURUGESAN","PRINCIPAL","MONDAY IS FULL WORKING DAY")
b=teacher("MURUGESAN","PRINCIPAL","MONDAY IS FULL WORKING DAY")
c=student("MURUGESAN","PRINCIPAL","MONDAY IS FULL WORKING DAY")
d=parents("MURUGESAN","PRINCIPAL","MONDAY IS FULL WORKING DAY")
a.msg("MURUGESAN","PRINCIPAL","MONDAY IS FULL WORKING DAY")