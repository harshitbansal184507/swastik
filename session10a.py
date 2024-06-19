def add(num1,num2,num3):
    result=num1+num2+num3
    print("result is: ",result)

add(10,20,30)
add(num3=50,num1=50,num2=80)

#default arguments / inputs
def square(num=5):
    result=num*num
    print("square is: ",result)

square()
square(3)
square(num=9)

def subtract(num1,num2=10):
    result=num1-num2
    print("result is: ",result)

subtract(num1=10)
