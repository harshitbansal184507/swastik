def add(num1,num2):
    result=num1+num2
    print("result is: ",result)

print(hex(id(add)))
print("add is: ",add) # add is a function and u will se the hashcode of the function

#execute the add function
add(10,20)
hello=add
hello(11,22)
#if you redefine the same function the previouse function will be removed from memory
#
def add(num1,num2,num3):
    result=num1+num2+num3
    print("result is: ",result)

print(hex(id(add)))
print("add is: ",add)
add(10,20,30)