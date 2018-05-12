class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp1 = Employee('Mher', 'Harutyunyan', 60000)
emp2 = Employee('Tamara', 'Sirakanyan', 70000)
print(Employee.num_of_emps)


# print(Employee.fullname(emp1))
# print(emp1.email)
# print(emp1.fullname())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


