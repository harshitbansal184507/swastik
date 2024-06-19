# 2. Create class of object
# Below class represents the object. It is description of object

class FlipkartObject():
    
    # Default Constructor in Python
    # self is reference variable, which will hashcode of current object
    def _init_(self):
        print("self:" , self)
        self.name = "Bag"
        self.price = 900
        self.id = 52134
        self.brand = "Skybags"
        self.colour = "blue"

    # Parameterized Constructor
    def _init_(self, name, price, id, brand, colour):
        print("self:" , self)
        self.name = name
        self.price = price
        self.id = id
        self.brand = brand
        self.colour = colour   

    def show(self):
        print("Product data: ")
        print(self.name , self.price)
    

product1 = FlipkartObject("bag" , 850, 5624, "skybags", "black")
print("product1: ", product1)
#print(vars(product1))
product1.show()

""" product2 = FlipkartObject()
print("product2: ", product2)
print(vars(product2))
"""
#hw:- Restaurant,  menu and dish eh 3 objects bnane hai