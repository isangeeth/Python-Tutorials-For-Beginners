#*args = Parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments
def add(num1, num2):
    sum = num1+num2
    return sum

print(add(4,6))# what if we have 3 parameters?

def sumofnum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sumofnum(1,2,3,4,5,6,7,8,9,10))
#we cant add or remove items from a tuple. convert the tuple to list by
#args = list(args) inside the function
