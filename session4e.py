#promo code: ZOMATO
#condition :more than 249
#condition2 : 50% off upto 150

amount=float(input("enter amount"))
promo_code=input("enter promo code")

if promo_code=="ZOMATO":
    print("promo code is valid")

    if amount >249:
        print("promo code applied")
        discount=0.50*amount
        
        if discount>=150:
            discount=150
            
        amount-=discount
        print("discount is:",discount)
        print("amount to be paid is",amount)
    else:
        print("amount is low..")