class Student:
    """Represents a college student."""
    school = "State University"
    def __init__(self, name , year, age):
        self.name = name
        self.year = year
        self.age = age
    def introduce(self):
        return f"Hi, i'm {self.name},"\
               f"year {self.year}"\
               f" and my age is {self.age}"

s1= Student("Ana",2,18)
s2 = Student("Jake",3,19)
print(s1.introduce())
print(s2.introduce())