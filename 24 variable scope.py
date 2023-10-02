#Scope is the region that a variable is recognised or available.
#it can be local and global
def display_name():
    name = "Sangeeth" #local scope
    print(name)
    return name

global_name = display_name() #global variable
print(global_name)
#LEGB Rule