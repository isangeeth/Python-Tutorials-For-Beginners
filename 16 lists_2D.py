drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "sandwich"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner,dessert]
print(food)
print(food[0])
print(food[0][0])
print(food[1][0])
print(food[2][0])
print(food[0][1])
print(food[1][1])
print(food[2][0])
print(len(food[1]))
for i in range(len(food)):
   for j in range(len(food[i])):
       print(food[i][j], end= " ")
   print("\n")