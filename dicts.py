mydict = {1: "cc", 2: "hh", 3: "uu"}

print(mydict)

mydict2 = dict( name ="sg", age = 11, city = "Kiev")
print(mydict2)

print(mydict[1])

mydict[7]="ok"
print(mydict)

mydict[7]="ghj"
print(mydict)

# del mydict[3]
# print(mydict)

# mydict.pop(1)
# print(mydict)

# n = int(input("Check dict: "))
# # if n in mydict:
# #     print(mydict[n])


# try:
#     print(mydict[n])
# except:
#     print("Error")


# for key, value in mydict.items():
#     print(key, value)

mydict_cpy = mydict.copy()

# mydict.update(mydict2)
# print(mydict)


mytuple = (8,7)
medict={mytuple:15}

print(medict)