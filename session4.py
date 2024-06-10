#operators
#arithematic operators
#+,_,*,/,**,//,%

product_price =200
gst=0.18
price_to_pay=product_price+gst
print(price_to_pay,type(price_to_pay),id(price_to_pay))

number=10
div=number//3
#// means integral division
print(div)

base=2
result=2**3
#** means raise to powe
print(result)

bucket_size=7
hashcode=120%7
print(hashcode)

#assignment operators
# =,+=,-=,*=,/=,//=,**=,%=

# a new reference variable age,will be created in stack
#a container 20 will be created in heap
#hashcode of 20 will be stored in age
#hence, age is a REFERENCE VARIABLE :)
age=20

#update operation
age +=10#short hand operator which will add and assign
age%=3
age-=1
print("age is",age)

#increment and decrement operators
qty=1
qty+=1
qty-=1
qty+=5
qty-=1
qty**=2
print("quantity is",qty)
