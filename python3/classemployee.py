# Python Object Oriented Programming # youtube.com/watch?v=ZDa-75JzLYM # v=BJ-VvGyQxho

class Employee:
    # pass
    raise_amount = 1.04
    num_of_emps = 0
#    """
    def __init__(self, first, last, pay):   # best to call the first arg SELF, it can be called anything?? but convetion is self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * 1.04)

#    """

# emp_1 = Employee()
# emp_2 = Employee()

print(Employee.num_of_emps)

emp_1 = Employee('Cor', 'Sch', 50000)
emp_2 = Employee('User', 'Test', 66000)

print(Employee.num_of_emps)
# print(emp_1)
# print(emp_2)

"""
emp_1.first = 'Co'
emp_1.last = 'Sch'
emp_1.email = 'Co.Sch@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000
"""

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {} {} {}'.format(emp_2.first, emp_2.last, emp_2.pay, emp_2.email))

print(emp_1.fullname())

emp_1.fullname()

print(Employee.fullname(emp_1))

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)

print(Employee.__dict__)

Employee.raise_amount = 1.15

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)

emp_1.raise_amount = 1.28

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)

print(Employee.num_of_emps)

