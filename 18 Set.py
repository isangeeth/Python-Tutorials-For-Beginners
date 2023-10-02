#Set = Collection which is unordered, unindexed. No duplicate values either

# utensils = {"fork", "spoon", "knife"}
# for x in utensils:
#     print(x)
#set is faster and dont allow duplicates
utensils = {"fork", "spoon", "knife", "spoon"}
# for x in utensils:
#     print((x))
#
# print("\n\n")
# utensils.add("napkin")
# utensils.remove("spoon")
# for x in utensils:
#     print((x))
# print("\n\n")
# #utensils.clear()
dishes = {"bowl", "plate", "cup", "knife"}
# utensils.update(dishes)
# for x in utensils:
#     print((x))
# print("\n\n")
# dishes.update(utensils)
# for x in dishes:
#     print((x))
# print("\n\n")
# print("\n\n")
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print((x))
print(utensils.difference(dishes)) #utensils has, but dishes doesnt
print(dishes.difference(utensils))
print(utensils.intersection(dishes)) #itens in common
