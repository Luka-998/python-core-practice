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

"""
Online Course Management
"""

class Course:
    PLATFORM_NAME = "CodeAcademy"
    TOTAL_COURSES = 0

    def __init__(self,title,level,duration_hours):
        if not isinstance(title,str):
            raise TypeError
        elif not title:
            raise ValueError
        self.title = title


        if not level in ('Beginner','Intermediate','Advanced'):
            raise ValueError
        self.level = level

        if not isinstance(duration_hours,(int,float)):
            raise TypeError
        elif duration_hours < 0:
            raise ValueError
        self.duration_hours = duration_hours

        self.TOTAL_COURSES +=1

    @classmethod
    def get_total_courses(cls):
        return cls.TOTAL_COURSES

    @classmethod
    def from_string(cls,incoming_string):
        "Python,Intermediate,40"
        splitted_string = incoming_string.split(sep=',')
        cls.language = splitted_string[0]
        cls.level = splitted_string[1]
        cls.duration = splitted_string[2]
                
        

if __name__ == '__main__':
    employee = Employee('Tech02')
    print(employee.cmp)
    print(Employee.get_cmp())