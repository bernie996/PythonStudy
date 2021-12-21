"""Make a list of countries
-Adding a country at the end
-Remove a country from the list by index
-Add a country in the middle
"""
'List of countries'
list1= ["Corea", "Denmark", "Italy", "Mexico", "Argentina"]
print(list1)

"Adding a country to the end"
list1.append("Netherlands")
print(list1)

"Remove a country from the list by index"
list1.remove("Denmark")
print(list1)

"Adding a country in the middle"
list1.insert(2, "France")
print(list1)
print()

'Set of Countries'
sett1 = {"Brazil", "Canada", "Nepal", "Japan", "Nigeria"}
print(sett1)

"Adding a country to the end"
sett1.update(["China"])
print(sett1)

"Removing a country"
sett1.remove("Nigeria")
print(sett1)


