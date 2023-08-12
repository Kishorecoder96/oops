class student:
    def __init__(self,Name,regno,grade) -> None:
        self.name=Name
        self.regno=regno
        self.grade=grade
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)
        print("Grade:",self.grade)
    def __init__(self,skills,experience):
        self.skills=skills
        self.experience=experience
        print("skills:",self.skills)
        print("Experience:",self.experience)
s1=student("python","2")
s1.name="Dheekshith"
s1.regno="221501062"
s1.grade="A"

s1.skills="Python"
s1.experience="2"
s1.display()
s1.__init__(s1.skills,s1.experience)
