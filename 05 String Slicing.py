#Slicing is used to create a substring by extracting elements from another string
#indexing[] or slice() or [start:stop:step]
name = "Sangeeth Ajith"
first_name = name[0]
print(first_name)
first_name = name[0:8] #0 is inclusive, 8 is exclusive
print(first_name)
first_name = name[:8]
print(first_name)
last_name = name[15:23]
print(last_name)
last_name = name[15:]
print(last_name)
#step is 1 by default
funky = name[0:8:2]
print(funky)
funky_max = name[::3]
print(funky_max)

reversed_name = name[::-1]
print(reversed_name)
website = "https://google.com"
slice = slice(8,-4) #8 in inclusive, other one is exclusive -4 is negative indexing from the back
print(website[slice])

web_2 = "https://wikipedia.com"
print(web_2[slice])