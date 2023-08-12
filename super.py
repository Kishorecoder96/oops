class boss:
    def __init__(self,name) -> None:
        self.name=name
    def display(self):
        print(self.name)
class staff(boss):
    def __init__(self,name):
        super().__init__(name)
        print(self.name)
b=staff("hukum thalaivar keluporom thalaivaru bayangaram")
b.display()