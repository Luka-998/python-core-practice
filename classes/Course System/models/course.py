class Course:
    PLATFORM_NAME = "CodeAcademy"
    TOTAL_COURSES = 0
    def __init__(self,title,level,duration_hours):
        if not title:
            raise ValueError("Title must not be empty string")
        self.title = title
        if level not in ("Beginner","Intermediate","Advanced"):
            raise ValueError
        self.level = level
        if not isinstance(duration_hours,(int,float)) and not isinstance(duration_hours,bool):
            raise TypeError
        elif duration_hours<=0:
            raise ValueError
        self.duration_hours = duration_hours
        Course.TOTAL_COURSES +=1
        
    @classmethod
    def get_total_courses(cls):
        return cls.TOTAL_COURSES
    """
    
    Alternative constructor
    
    """
    @classmethod
    def from_string(cls,stringz):
        list_string = stringz.split(sep=',')
        name = list_string[0]
        level = list_string[1]
        if level not in ("Beginner","Intermediate","Advanced"):
            raise ValueError
        duration_hours = int(list_string[2])
        return cls(name,level,duration_hours)
        

if __name__ == "__main__":
    c1 = Course('z','Beginner',41230)
    c2 = Course.from_string("Python,Beginner,421312312")
    print(c2.level,c2.title,c2.duration_hours)