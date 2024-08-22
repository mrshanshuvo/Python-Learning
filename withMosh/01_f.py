def greet(name):
    print(f"Hi, {name}")


def get_greeting(name):
    return (f"Hi, {name}")


greet("Shuvo")
message = get_greeting("Shuvo")

file = open("content.txt", "w")
file.write(message)
file.write("My name is shahid Hasan Shuvo")
