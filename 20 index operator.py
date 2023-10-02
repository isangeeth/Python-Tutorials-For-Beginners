#Index operator[] gives Access to a sequence's element from (str, list, tuples)
name = "sangeeth ajith"
# if (name[0].islower()):
#     name = name.capitalize()
print(name)
first_name = name[0:8].upper() #zero is not needed
print(first_name)
last_name = name[9:].lower()
print(last_name)
#negative indexing
last_ch = name[-1]
print(last_ch)