class Employee:
    raised_number=1
    number_of_emps=0
    def __init__(self,fname,mname,lname,pay):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        self.email=fname + "." + lname + "@company.com"
        self.pay=pay
        Employee.number_of_emps+=1
    def full_name (self):
        return "Full Name - "+"{} {} {}".format(self.fname,self.mname,self.lname)
    def pay_raise(self):
        self.pay=int(self.pay*self.raised_number) 


print(Employee.number_of_emps)
emp_01=Employee("Shreshth","Kumar","Chaudhary",10000)
print(Employee.number_of_emps)
emp_02=Employee("Shreyash","","Chaudhary",19999)
print(Employee.number_of_emps)

# print(emp_02.full_name())


print(emp_01.__dict__)
emp_01.raised_number=1.10
print(emp_01.__dict__)

print(emp_01.pay)
emp_01.pay_raise()
print(emp_01.pay)

