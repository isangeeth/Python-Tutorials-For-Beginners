#strings
first_name = "San"
last_name = "Angels"
name = first_name+" "+last_name
#print(name)
#print("\n hello "+name)
#print(type(name))
l = len(name)
#print(l)
#print(len(name))
print(name.find("g")) #to find the index
print(name.capitalize()) #Capitalize first word of each string
print(name.lower()) #all letter lowercase
print(name.upper())
name_1 = "777"
print(name_1.isdigit()) #string is a digit or not
name_2 = "SanAngels777"
print(name_2.isalpha())# to check whether string contains only alphabetical letters
print(name.count("ls")) #return number of counts
print(name.replace("ee","i"))
print(name*5)