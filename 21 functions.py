#function is a block of code, executed only when it is called.
# def hello():
#     print("Hello!")
#     print("Have a nice day!!!")
#
# hello()
def hello1(name):
    print("Hello "+name)

hello1("Sangi")

#use more than one parameters and try playing with the parameters
def multiply(x, y):
    m = x*y
    return m
a = int(input("Enter first number : "))
b = int(input("Enter the second number : "))
multi = multiply(a,b)
print("The multiplied of the above is : ", multi)