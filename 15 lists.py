#list = used to store multiple values in a single variable
food = ["pizza", "burger", "sandwich", "pasta"] # it is a list
print(food)
#print(food[2]) #print a particular item from list
food[0] = "kanji"
#print(food)
for i in food:
    print(i)
print("loop 1\n")

food.append("vadapav")
food.remove("pasta")
food.pop() #remove last element
food.insert(1, "cake")
food .sort()
food.clear()
for i in food:
    print(i)
