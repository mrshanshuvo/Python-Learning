class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark

        print(self.name, ",Your average score is: ", (sum/3))


s1 = Student("Shuvo", [98, 95, 94])
s1.hello()
s1.get_avg()
