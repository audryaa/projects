#INHERITANCE
#allows a class to acquire properties and methods from another class

class Dog:
    def __init__(self,sound):
        self.sound = sound
        print("Woof!")

    class Cat:
        def __init__(self,sound):
            self.sound = sound

            print("Meow!")

#PARENT CLASS
#it contains the original properties and methods that will be inherited by the child class
#contains shared features

class Animal:
    def eat(self):
        print("It's eating")

#CHILD CLASS
#inherits the properties and methods from the parent class

class Dog(Animal):
    pass

#METHOD OVERRIDING
#allows a child class to provide a specific implementation of a method that is already defined in its parent class
class Animal:
    def speak(self):
        print("SOUND : ")

class Dog(Animal):
    def speak(self):
        super().speak() #calls the speak method from the parent class
        print("WOOF!WOOF!")

dog = Dog()
dog.speak()

#SUPER()
#allows you to call a method from the parent class
#means "go to my parent class"

#CONSTRUCTOR INHERITANCE
#allows a child class to inherit the constructor of its parent class
#__init__() is a special method that is automatically called when an object is created from a class

class Animal:
    def __init__(self,name):
        self.name = name
        
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        
dog = Dog("Rex")
print(dog.name)