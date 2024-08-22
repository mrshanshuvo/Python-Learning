data = True
line_no = 1
with open("practice.txt", "r") as f:
    while data:
        data = f.readline()
        if ("learning" in data):
            print(line_no)
        line_no += 1
