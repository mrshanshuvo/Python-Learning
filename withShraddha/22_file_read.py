# f = open("file_name", "mode")

# f = open("E:\PL Codes\pythonVS\withShraddha\22_demo.txt", "r")  wrong
f = open("E:\\PL Codes\\pythonVS\\withShraddha\\22_demo.txt", "r")
# read() covers the whole data
# data = f.read()
# print(data)

print(f.readline())  # line1
# readline() reads one line at a time
print(f.readline())  # line2
f.close()
