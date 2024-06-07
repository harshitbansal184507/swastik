promo_code1="ZOMATO40"
print(promo_code1, type(promo_code1), id(promo_code1))

#reference copy operation
promo_code2=promo_code1
print(promo_code2, type(promo_code2), id(promo_code2))
#so address / hashcode will not be changed

#delete statement
del promo_code1
print(promo_code2, type(promo_code2), id(promo_code2))
