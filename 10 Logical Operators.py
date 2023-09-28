temp = int(input("What is the tempereture outside?? :"))
if temp>=0 and temp<=30:
    print("The tempereture is good today!\n Go outside!!")
    #both must be true
elif temp< 0 or temp> 30:
    print("the temperature is bad today\n stay inside!")
#use "not"  to reverse the roles
# if not(......) true to false and false to true
