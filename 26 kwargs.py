#kwargs = parameter that will pack all the arguments into a dictionary
#useful so that a function can accept varying amount of keyword arguments
#arg accept varying amount of positional argumnetsand pack them into a tuple.
#but kwargs will accept varying amount of keyword arguments and pack them into a dictionary
def hello(first, last):
    print("Hello "+ first+" "+last)

hello(first = "Sangeeth", last = "Ajith") # cant accept amiddle name

def hello2(**kwargs):
    print("Hello" + kwargs['first'] + " " + kwargs['last'])
hello2(first = "Sangeeth", middle = "Ajith", last = "V V")

def hello3(**kwargs):
    print("Hello ", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")
hello3(first = "Sangeeth", middle = "Ajith", last = "V V")
print('\n')

def hello4(**kwargs):
    print("Hello", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")
hello4(title = 'Mr', first = "Sangeeth", middle = "Ajith", last = "V V")

def hello5(**anyname):
    print("Hello ! ", end = " ")
    for key, value in anyname.items():
        print(value, end = " ")
hello5(title = 'Mr', first = "Sangeeth", middle = "Ajith", last = "V V")