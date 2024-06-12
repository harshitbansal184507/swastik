''''''''''
    ZOMATO: 20% off 
        : min value: 300
    BINGO: 50% off 
        : min value: 500
        :max discount: 100 

#indentation: PEP(python enhancement proposal)
'''''''''
#if/else:- workflows
promo_code=input("enter promo code: ")
amount=float(input("enter your amount: "))

if promo_code=="ZOMATO":
    print("ZOMATO CAN BE APPLIED")

    if amount>300:
        discount=0.20*amount
        print("ZOMATO applied you got a discount of : ",discount)
        print("you can pay: \u20b9",amount-discount)
    else:
        print("amount is less, please add items worth",(300-amount),"more..")

elif promo_code=="BINGO":
    print("BINGO CAN BE APPLIED")
    if amount>500:
        discount=0.50*amount

        if discount>100:
            discount=100
        print("BINGO applied you got a discount of : ",discount)
        print("you can pay: \u20b9",amount-discount)
    else:
        print("amount is less, please add items worth",(500-amount),"more..")
else:
    print("INVALID PROMO CODE")  

