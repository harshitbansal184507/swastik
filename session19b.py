"""
Empty structures


my_tuple=()
my_tuple=tuple()


"""
my_data={
    101:"john",
    102:"jennie",
    501:"sia",
    99:"joe",
    25:"kim"
}

print(my_data)
print(len(my_data))
print(max(my_data))
print(min(my_data))
print(sum(my_data)) #----> works only on integer keys
my_data.pop(102)
my_data[201]="joseph"
print(my_data)
"""
my_data={
    "jo":"john",
    "je":"jennie",
    "si":"sia",
    "j":"joe",
    "ki":"kim"
}"""

attendance=["june","july","august"]
college_attendance={}.fromkeys(attendance,100)
college_attendance["august"]=70
print(college_attendance)

items=list(my_data.items())
Values=list(my_data.values())
print(items)
print(Values)

for item in my_data.items():
    print(item)

for value in my_data.values():
    print(value)