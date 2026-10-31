
class Employee:
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

    
class Manager(Employee):
    def __init__(self,name,surname,salary,monthly_bonus):
        super().__init__(name,surname,salary)
        if monthly_bonus < 0:
            raise ValueError("Bonus cant be negative")
        self.bonus = monthly_bonus
    def count_annuall(self):
        return super().count_annuall() + (self.bonus * 12)
    
        
if __name__ == "__main__":
    s = Employee("Luka","Jasovic",1000) 
    print(s.get_full_name())   
    print(s.count_annuall())
    z = Manager("Pavle","Jasovic",1000,200)
    print(z.get_full_name())
    print(z.count_annuall())
