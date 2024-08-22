# info = {
#     "name": "Shahid Hasn Shuvo",
#     "cga": 3.70,
#     "age": 24,
#     "subjects": ["python", "c", "java"],
#     "topics": ("dict", "set"),
#     5: 78
# }

# info["name"] = "Shuvo"
# info["studentID"] = "221002038"

# print(info)

# print(info["name"])

student = {
    "name": "zahid hasan",
    "subjects": {
        "phy": 97,
        "chem": 94,
        "math": 99
    }
}

# print(student)
# print(student["subjects"]["phy"])


# print(student.keys())
# print(student.values())
# print(student.items())

# pairs = list(student.items())

# print(pairs[0])

student.update({"city": "Dhaka"})

print(student)
