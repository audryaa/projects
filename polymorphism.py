class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is managing")

class Developer(Employee):
    def work(self):
        print("Developer is coding")

class Designer(Employee):
    def work(self):
        print("Designer is designing")

#creating objects
manager = Manager()
developer = Developer()
designer = Designer()

manager.work()
developer.work()
designer.work()