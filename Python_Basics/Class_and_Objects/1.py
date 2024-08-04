class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID : {self.id}, Name : {self.name}")

emp = Employee("23MM02007", "coder")

emp.display()

del emp.name
try:
    print(emp.name)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.display()
except NameError:
    print("emp is not defined")