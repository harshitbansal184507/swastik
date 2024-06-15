"""
i have HDFC credit card 
hdfc bank will charge 15 % interest on outstanding amount
minimum you should be able to pay 10% of outstanding amound else your credit card will be compromised
april 2024 -> 50,000  ----> input by user
      april 2024 min -> 5000
                 pending ----> 45000
                               +15% of 45000 = 6750
i can only pay max of 8000 per month ----> input by user
find in which month whole amount will become 0

"""
print("you will get the amount at the interest of 15%")
amount=int(input("please enter the amount you want to take from credit card: "))
print("LOAN AMOUNT: ",amount)
print("BOOKED ON: 12 april,2024")
first=int(input("enter the amount you want to pay for your first installment: "))
new_amount=amount-first
i=4

total=new_amount
max=int(input("enter the maximum amount you want to pay for you next installments: "))
print("----------------------------------")
month=new_amount/max
rate=15/month
while(new_amount>0):
    interest=(rate/100)*new_amount
    print("interest: ",interest)
    loan_amount=max-interest
    print("loan amount: ",loan_amount)
    print("installment amount: ",max)
    new_amount=new_amount-loan_amount
    i=i+1
    total+=new_amount
    if i<13:
        print("due date: 12-",i,"-2024")
    else:
        print("due date: 12-",i-12,"-2025")
    print("--------------------------------")
if i<12:
    print(" your installements will be compeleted on 12-",i,"-2024")
else:
     print(" your installements will be compeleted on 12-",i-12,"-2025")
print(new_amount)