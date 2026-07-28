#classes

#OOP - OBJECT ORIENTED PROGRAMMING

#CLASS - a blueprint for creating objects
#PHONE 
  #has a battery , brand, RAM , storage - ATTRIBUTES (characteristics)
  # can call, charge, take video, play music - METHODS (actions)

#FACEBOOK
#users have; name, email, password, age
#users can log in, log out, post

#AUDRY
#name = Audryy
#email = audry123@gmail.com

#MAYA
#name = breakpoint

#TOYOTA
#windows, doors, engines, seats - design
#dedign = class
#each car is an object
#one class creates many object

#class Students:

#class tells python that you're creating a class
#Students - class name
# : - starts class body
#pass - tells python you are not adding anything

#OBJECT
#student1 = student()

#student1 stores an object in a variable 
#student() creates a new student

#THE CONSTRUCTOR 
#_init_()

#class Student:
    #def __init__(self,name,course):
        #self.name = name
        #self.course = course

#SELF 
#self allows each object to keep its own data (prevents overwriting)

#creating an object
#student1 = Student("BRITNEY,""CYBER SECURITY")

#python thinks like this 
#self.name = "BRITNEY"
#DIFFERENT OBJECTS DIFFERENT MEMORY DIFFERENT DATA 

#ATTRIBUTES
#variables inside an object

#ACCESSING THE ATTRIBUTES
#print(self.name)

#output - 

#METHODS
#functions inside classes 



class Student:
    def __init__(self,name,course):

        self.name = name
        self.course = course 

    def introduce(self):

        print(f"My name is {self.name}")

        print(f"I study {self.course}")
        
student1 = Student("BRITNEY","CYBER SECURITY")
student2 = Student("JOHN","COMPUTER SCIENCE") 
student3 = Student("JOB","DATA SCIENCE")
student4 = Student("MERCY","SOFTWARE ENGINEERING")
student5 = Student("ALEX","IT")


student1.introduce()
student2.introduce()
student3.introduce()
student4.introduce()
student5.introduce()     