# A changeable, unordered collection of unique key value pairs.
#They are fast because they use hashing
capitals = {'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow'}
# print("Capital of Russia is : ", capitals['Russia'])
# print(capitals['Germany']) won't work, create error. to prevent that we use get() function
# print(capitals.get('Germany')) #none
print(capitals.keys()) #country names
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,"-", value)

#dictionaries are mutable, means we can alter them after the program is already running, using update
capitals.update({'Germany': 'Berlin'})
print("\n The updated List 1 is \n")
for key,value in capitals.items():
    print(key,"-", value)
print("\n The updated List 2 after changing capital of USA is \n")
capitals.update({'USA':'New york'})
for key,value in capitals.items():
    print(key,"-", value)
#print(capitals)
print("\n The updated List 3 after removing china \n")
capitals.pop('China')
for key,value in capitals.items():
    print(key,"-", value)
print("After Clearing the dictionary")
capitals.clear()
for key,value in capitals.items():
    print(key,"-", value)

