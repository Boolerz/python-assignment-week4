#parent class 1
class Person:
    def person_info(self,name,age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)
        
#parent class 2
class Company:
    def company_info(self,company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)
        
#Child class
class Employee(Person, Company):
    def Employee_info(self, salary,skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)
        
#create object of Employee
emp = Employee()

#access data
emp.person_info('Rashid', 31)
emp.company_info('Boolerz', 'Mariakani')
emp.Employee_info(40000, 'Managing Director')