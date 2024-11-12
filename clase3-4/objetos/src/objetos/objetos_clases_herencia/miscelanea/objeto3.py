#################################
## Animal abstract data type
#################################
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


print("\n---- animal tests ----")
a = Animal(4)
print(a)
print(a.get_age())
a.set_name("fluffy")
print(a)
a.set_name()
print(a)


#################################
## Inheritance example
#################################
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


print("\n---- cat tests ----")
c = Cat(5)
c.set_name("fluffy")
print(c)
c.speak()
print(c.get_age())