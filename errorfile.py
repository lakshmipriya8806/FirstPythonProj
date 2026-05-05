class Animal():
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f"{self.name} is barking")

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
   
   def sleep(self):
       print(f"{self.name} is sleeping")

dog1=Dog("Tom")


print(dog1.eat())
print(dog1.sleep())