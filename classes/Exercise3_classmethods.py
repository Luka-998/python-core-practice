"""
self -> instance attributes ( object state)
cls -> class attributes (class state)

class attribute can be accessed both with classmethod and just caling as __className__.attribute
instance method/attribute is usually called via instance
"""

# simple example

class Employee:
    COMPANY = "Tech01"
    def __init__(self,cmp):
        self.cmp = cmp

    def get_name(self):
        return self.cmp

    @classmethod
    def get_cmp(cls):
        return cls.COMPANY




if __name__ == '__main__':
    employee = Employee('Tech02')
    print(employee.cmp)
    print(Employee.get_cmp())