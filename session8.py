"""
   Principle of OOPS:
   1. Think of an object

   instagram_post: likes, views, comments, shares, posting time
   flipkart_product: name, price, brand, id, seller_name
   zomato_order: name, id, customer, restaurant_name, price
"""

# 2. Create class of object
# Below class represents the object. It is description of object
class FlipkartProduct:
    pass

# 3. Create the real object from class in Memory
# Below is: Object Construction Statement
product1 = FlipkartProduct()
product2 = FlipkartProduct()

product3 = product1
# product1 is a reference variable, FlipkartProduct() - reperesent the object construction
print(product1)
print(id(product1))
print(hex(id(product1)))

# Operations on Object
# 1. Write Operation
product1.name = "Bag"
product1.price = 900
product1.id = 52134
product1.brand = "Skybags"
product1.colour = "blue"

product2.name = "Bag"
product2.price = 900
product2.id = 52134
product2.brand = "Skybags"
product2.colour = "blue"
product2.seller = "Dawnson"

# 2. Update Operation
product1.price = 850
product3.colour = "black"

# 3. Read Operation
print("Product1 data: ")
print(vars(product1))

print("Product2 data: ")
print(vars(product2))

# 4. Delete Operation
del product1.brand
print("Product1 data: ")
print(vars(product1))

del product2
"""
print("Product2 data: ")
print(vars(product2))
ERROR
"""