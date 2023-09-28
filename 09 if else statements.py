age = input("How Old Are you??? : ")
age = int(age)
if age==100:
    print("You are A CENTURY old!!!!")
if age >=18:
    if age == 100:
        print("You are A CENTURY old!!!!")
    else:
        print("You are an adult")
elif age<=0:
    print("You are not born yet!")
else:
    print("You are a Child")

    #put else at last only