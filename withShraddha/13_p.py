marks = {}

x = int(input("Enter 1st number: "))
marks.update({"phy": x})

x = int(input("Enter 2nd number: "))
marks.update({"chem": x})

x = int(input("Enter 3rd number: "))
marks.update({"math": x})

print(marks)
