#add to cart
cart=[]
price=[]
quantity=[]
menu={"noodles":50,
      "burger":40,
      "momos":60,
      "sandwitches":50}

print("welcome to foodies....")
print(" our menu is:")
print("-------------------------")
print(menu)

while True:
    item=input("enter tiems to add to cart or 0 to quit")
    
    if item=="0"
    break

    qty=int(input("enter quantity of items"))
      quantity.append(qty)
cart.append(item)
price.append(menu[item]*qty)

print("items in your cart are:")
print(cart)
print("QUANTITY")
print(quantity)
print("price is:")
print(price)
print("number of items in cart are :",len(cart))
print("total amount to be paid is:",sum(price))
