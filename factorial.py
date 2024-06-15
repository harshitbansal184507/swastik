def fact(number):
    if number==1:
        return 1
    else:
        return(number*fact(number-1))
    
number=int(input("enter a number for factorial: "))
factorial=fact(number)
print("factorial of ",number," is: ",factorial)
