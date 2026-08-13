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

    @classmethod
    def set_raised_amount(cls,amount):
        cls.raised_number=amount

    @classmethod
    def from_string(cls,emp_str):
        fname,mname,lname,pay=emp_str.split("-")
        return cls(fname,mname,lname,pay)
    

emp_01=Employee("Shreshth","Kumar","Chaudhary",10000)
emp_02=Employee("Shreyash","","Chaudhary",10000000)
    

# emp_01.set_raised_amount(1.3)
# Employee.set_raised_amount(1.2)
# print(emp_01.raised_number)
# print(emp_02.raised_number)


emp_str_1 = 'John-1-Doe-70000'
emp_str_2 = 'Steve-2-Smith-30000'
emp_str_3 = 'Jane-3-Doe-90000'


# # Manual Method
# fname,mname,lname,pay=emp_str_1.split("-")
# new_emp_01=Employee(fname,mname,lname,pay)
# print("Name -",new_emp_01.fname,new_emp_01.mname,new_emp_01.lname)
# print("Email -",new_emp_01.email)
# print("Pay -",new_emp_01.pay)


new_emp_01 = Employee.from_string(emp_str_1)
new_emp_02 = Employee.from_string(emp_str_2)
new_emp_03 = Employee.from_string(emp_str_3)
print("Name -",new_emp_01.fname,new_emp_01.mname,new_emp_01.lname)
print("Email -",new_emp_01.email)
print("Pay -",new_emp_01.pay)
print("Name -",new_emp_02.fname,new_emp_02.mname,new_emp_02.lname)
print("Email -",new_emp_02.email)
print("Pay -",new_emp_02.pay)
print("Name -",new_emp_03.fname,new_emp_03.mname,new_emp_03.lname)
print("Email -",new_emp_03.email)
print("Pay -",new_emp_03.pay)