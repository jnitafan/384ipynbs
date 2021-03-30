# initialize all variables with months
mylist = ["Jan", "Feb", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
mytuple = ("Jan", "Feb", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December")
myset = {"Jan", "Feb", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"}
mydict = {"Jan": 1, "Feb": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
          "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

# print the months from the list
print(type(mylist))
for month in mylist:
    print(month)

# print the months from the tuple
print(type(mytuple))
for month in mytuple:
    print(month)

# print the months from the set
print(type(myset))
for month in myset:
    print(month)

# print the months from the dict
print(type(mydict))
for month in mydict.keys():
    print(month)
