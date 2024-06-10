#conditional operators
#==,!=,>,<,>=,<=

cab_fare =500
e_wallet=200
result=e_wallet>=cab_fare
print("can i book the cab: ",result)
print(type(result))

email=input("enter your email")
password=input("enter your password")
print("is login successfull?")
result= email==("john@example.com") and (password=="john123")
#result= email==("john@example.com") or (password=="john123")
print(result)

otp=3027
user_otp=int(input("enter otp received"))
print("is otp correct??", otp== user_otp)

#membership testing
# is , is not

a=10
b=10
print(a==b)
print(a is b)
#hw: find diffrence between == and is