import random
x = random.randint(1,6)
print(x)
y= random.random()
print(y) #between 0 and 1
myList = ["Rock", "Paper", "Scissors"]
z= random.choice(myList)
print(z)

cards = [2,3,4,5,6,7,8,9,"A","K","Q","J"]
random.shuffle(cards)
print(cards)