# arithmethic operators +,-,*,/,%,**
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a % b)  # remainder
print(a ** b)  # a ^ b

# relational/comparison operators ==, !>, >, <, >=, <=
a = 50
b = 20

print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# assignement operators =, +=, -+, *=, /=, %=, **=

num = 5

num += 2

print(num)
num -= 2

print(num)
num *= 2

print(num)
num /= 2

print(num)
num **= 2

print(num)


# logical operators not/and/or
print(not False)
print(not True)


# type conversiotn
a = "2"
b = 4.25
c = int(a)
sum = c + b
print(sum)

# input

a = input("Enter any value: ")
print(type(a))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
