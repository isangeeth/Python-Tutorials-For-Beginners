#Exception is the events detected during execution that interrupt the flow of a program
try:
    num = int(input("Enter a number to divide : "))
    denom = int(input("Enter a number to divide by : "))
    result = num/denom
    print(result)
except ZeroDivisionError as a:# as e
    print(a)
    print("You cant divide using Zero!")
except ValueError as b:
    print(b)
    print("Enter only numbers pls!")
# except Exception:
#     print("Something went wrong")
else:
    print("Result is ",result)
finally: #execute any code
    print("This will always execute!")