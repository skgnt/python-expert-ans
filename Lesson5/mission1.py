class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(self.name)
        print("わんわん")

inu=Dog("Max")
inu.bark()