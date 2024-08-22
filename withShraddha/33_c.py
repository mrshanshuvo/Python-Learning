class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Loading.....")


s1 = Student("Shahid Hasan Shuvo", 98)
print(s1.name, s1.marks)

s2 = Student("Zahid Hasan Joy", 99)
print(s2.name, s2.marks)
