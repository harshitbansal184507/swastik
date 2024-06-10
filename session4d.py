#condition1:  you can apply promo code only and only if minimum amount is 500
#condition2:

promo_code = "GET200"
min_amount= 500
amount = float(input("enter your amount:"))

#conditional statement : if/else
if amount>min_amount:
    print("you can apply promo code",promo_code)
    amount-=200
    print("promo code applied successfully please pay",amount)
else:
    print("you cannot apply promo code",promo_code)
    print("add items worth",(min_amount-amount),"more..")