# method 1
class Student:
    def __init__(self, name, math, ict, eng):
        self.name = name
        self.math = math
        self.ict = ict
        self.eng = eng

    def get_avg(self):
        print(self.name, "Average score is: ", (self.math+self.ict+self.eng)/3)


s1 = Student("Shuvo", 98, 95, 94)
s1.get_avg()


# method 2
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark

        print(self.name, ",Your average score is: ", (sum/3))


s1 = Student("Shuvo", [98, 95, 94])
s1.get_avg()


# method 3
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum/3


s1 = Student("Shahid Hasan Shuvo", [99, 97, 45])
avg_mark = s1.get_avg()
print(s1.name, ",Your average mark is : ", avg_mark)
