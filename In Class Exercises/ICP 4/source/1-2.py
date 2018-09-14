class Employee:
    Ecount = 0
    tsal = 0
    avgsal = 0

    def __init__(self, name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.Ecount +=1
        Employee.tsal += int(salary)

    def average_salary(self):
        print("Average Salary of %d is:" % (Employee.tsal / Employee.Ecount))

    def explain_inheritance(self):
         print("this is output from parent class")

    def print_emp(self):
        print("\n name:", self.name, "family:",self.family, "salary:",self.salary,"department:",self.department)

class Parent_Employee(Employee):
    def another_method(self):
        print("Output from child class")



    def displayCount(self):
        print("Total Employee %d" % Employee.Ecount)



emp1 = Employee("Kamal", "abcde ", "1000", "CSEE")
emp2 = Employee("Vinay", "fghij", "2000", "EE")
emp3 = Employee("Matty", "klmnop", "2500", "CS")
emp4 = Employee("Tej", "qrstu", "3000", "CS")

emp5 = Parent_Employee("Veer",)
# this is by function calling
emp4.average_salary()
# displaying output
emp1.print_emp(

)

# accessing child class
emp5.explain_interitance()
emp5.another_method()