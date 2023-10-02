#for strings
animal = "cow"
item ="moon"
#print("The "+animal+" Jumped over the "+item)
print(("The {} jumped over the {}".format("cow", "moon")))
print(("The {} jumped over the {}".format(animal, item)))  #positional argument
#{} format fields
print(("The {0} jumped over the {1}".format(animal, item)))
print(("The {animal} jumped over the {item}".format(animal = "cat", item= "Sun")))
text = "The {} jumped over the {}"
print(text.format(animal, item))
name= "Sangeeth"
print("Hello, my name is {:30}. Nice to meet you".format(name)) #:30 reffers to the spacing ===> adding a padding
print("Hello, my name is {:<30}. Nice to meet you".format(name))
print("Hello, my name is {:>30}. Nice to meet you".format(name))
print("Hello, my name is {:^30}. Nice to meet you".format(name))
#print("Hello, my name is {'name':30}. Nice to meet you".format(name))

#Numbers
number = 3.14159
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))
n = 1000
print("The number is {:,}".format(n))
print("The number is {:b}".format(n)) #b- binary, o-octahedral, ;X- Hexa decimal, :e or :E for scientific
print("The number is {:e}".format(n))