try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age can not be zero")
else:
    print("No exceptions were thrown")
print("Excution continues.")

# A more clean code
try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
print("Excution continues.")
