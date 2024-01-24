class Student:
    def __init__(self, name, marks, roll_no) -> None:
        self.name = name
        self.marks = marks
        self.roll_no = roll_no
    
    def get_info(self) -> str:
        info = f'''
        Student name: {self.name}
        Roll no.: {self.roll_no}
        Marks: {self.marks}
        '''
        
        return info

obj1 = Student(name="Harry Porter", marks=89, roll_no=111)
obj2 = Student(name="Simpson", marks=99, roll_no=222)

str1 = obj1.get_info()
str2 = obj2.get_info()

print(str1)
print(str2)
