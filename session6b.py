def square(num):
    print("1. num is: ",num, id(num)) #10
    for idx in range(0,len(num)):
        num[idx]= num[idx]*num[idx]
    print("2. num is: ",num, id(num)) #100

#functions in memory
#print("square: ",square)

number=[10,20,30,40,50]
print("A. number is: ",number, id(number)) #10
square(number)
print("B. number is",number,id(number)) #10
