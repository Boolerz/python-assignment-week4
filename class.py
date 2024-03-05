#python class
class Person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def greet(self):
        return f"Hello, my name is {self.name} and my age is {self.age} my gender is {self.gender}"
    
person1=Person("john",22,"male")
person2= Person("fondo", 34, "male")
print(person2.greet())
print(person1.greet())
