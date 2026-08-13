# class Employee:
#     True

# employee_01=Employee()
# employee_02=Employee()

# employee_01.fname="shreshth"
# employee_01.mname="kumar"
# employee_01.lname="chaudhary"
# employee_01.email=employee_01.fname + "." + employee_01.lname + "@company.com"

# print(employee_01.fname)
# print(employee_01.mname)
# print(employee_01.lname)
# print(employee_01.email)





class Employee:
    def __init__(self,fname,mname,lname,pay):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        self.email=fname + "." + lname + "@company.com"
        self.pay=pay
    def full_name (self):
        return "Full Name - "+"{} {} {}".format(self.fname,self.mname,self.lname)

emp_01=Employee("Shreshth","Kumar","Chaudhary",9999)
print("Name -",emp_01.fname,emp_01.mname,emp_01.lname)
print("Email -",emp_01.email)
print("Pay -",emp_01.pay)

print("Full Name -","{} {} {}".format(emp_01.fname,emp_01.mname,emp_01.lname))
 
print(emp_01.full_name())
print(Employee.full_name(emp_01))