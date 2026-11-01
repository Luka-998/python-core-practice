
class Employee:
    COMPANY = "BookStore"
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        if salary < 0:
            raise ValueError("Salary must not be negative")
        self.salary = salary

    def get_full_name(self):
        return f"{self.name},{self.surname}"

    def count_annuall(self):
        return self.salary * 12

    @classmethod
    def get_company(cls):
        return cls.COMPANY
    
class Manager(Employee):
    def __init__(self,name,surname,salary,monthly_bonus):
        super().__init__(name,surname,salary)
        if monthly_bonus < 0:
            raise ValueError("Bonus cant be negative")
        self.bonus = monthly_bonus
    def count_annuall(self):
        return super().count_annuall() + (self.bonus * 12)


class SalesEmployee(Employee):
    COMPANY = "BookStore Sales"
    def __init__(self,name,surname,salary,comission):
        super().__init__(name,surname,salary)
        if comission < 0:
            raise ValueError("Comission can't be negative!")
        self.comission = comission

    def count_annuall(self):
        return super().count_annuall() + self.comission
    


class SeniorSalesEmployee(SalesEmployee):
    def __init__(self,name,surname,salary,comission,seniority_bonus):
        super().__init__(name,surname,salary,comission)
        if seniority_bonus < 0:
            raise ValueError
        self.seniority_bonus = seniority_bonus

    def count_annuall(self):
        return super().count_annuall() + self.seniority_bonus * 12


    
        
if __name__ == "__main__":
    s = Employee("Luka","Jasovic",1000) 
    print(s.get_full_name())   
    print(s.count_annuall())
    z = Manager("Pavle","Jasovic",1000,200)
    print(z.get_full_name())
    print(z.count_annuall())
    salesemp = SalesEmployee("Luka","Jasovic",1000,0.05)
    print(salesemp.count_annuall())
    print(s.COMPANY)
    print(salesemp.get_company())
    print(s.get_company())
    print(z.get_company())
    print('----')
    seniorSales = SeniorSalesEmployee("Luka","Jasovic",12000,0.05,1500) 
    print(seniorSales.get_company())
    print(seniorSales.count_annuall())