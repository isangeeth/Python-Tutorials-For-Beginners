#tuple = collection which is ordered and unchangeable, used to group together related data


student = ("Abhi", 21, "male")
print(student.count("Abhi"))
print(student.index("male"))
for x in student:
    print(x)

if "Abhi" in student:
    print("Name True")