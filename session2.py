numbers = [10,20,30,40,50]
print(numbers,type(numbers),id(numbers))

#REFERENCE COPY OPERATION -> copy ahshcode
my_numbers = numbers
print(my_numbers,type(my_numbers),id(my_numbers))

print(id(numbers[2]))
numbers[2]=1122
print(id(numbers[2]))

print(numbers[2])
print(my_numbers[2])
#so if we'll change data in one  list both will be changed