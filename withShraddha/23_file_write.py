# f = open("E:\\PL Codes\\pythonVS\\withShraddha\\22_demo.txt", "r")

# data = f.read()

# print(data)

# f.close()

# f = open("demo.txt", "w")

# f.write("Hello, My name is Shahid Hasan Shuvo.........")

# f.close()
# f = open("demo.txt", "a")

# f.write("\nHello, My name is Shahid Hasan Shuvo.........")

# f.close()
f = open("demo.txt", "w+")

f.write("Hello, My name is Shahid Hasan Shuvo.........")

data = f.read()

print(data)
f.close()
