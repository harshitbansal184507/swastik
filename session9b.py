"""
  code 3 objects:
  1.dish: name , price , rating
  2.menu: name , number of dishes , dishes  
    | 1 menu can have many dishes(1 to many)
  3.restaurant: name , phone email , addres , operating_hours , ratings , menu 
    | 1 restaurent can have 1 menu(1 to 1)
"""
from session9a import Menu
from session9 import dish



class Restaurant:
    def __init__(self, name="NA",phone="NA",email="NA",address="NA",operating_hours=0,ratings=0,menu=" "):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.operating_hours=operating_hours
        self.ratings=ratings
        self.menu=menu
    def show(self):
        print("RESTAURANT")
        print("-----------------------------------")
        print("Restaurant: ",self.name," | ", self.phone," | ", self.email)
        print("Address: ",self.address, " | " ,self.operating_hours," | ",self.ratings)
        print("-----------------------------------\n")
        self.menu.show()
    
"""
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]
"""

"""
menu = Menu(
    name="Indian Veggie Delight", 
    number_of_dishes=len(dishes), 
    menu_dishes=dishes)
"""


restaurant = Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        dish(), 
                                        dish("Dal Makhani", 250, 4.5),
                                        dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        )

restaurant.show()

"""
menu_dishes=[dish(), dish("Dal Makhani", 250, 4.5),dish("Paneer Masala", 350,4.5)]
menu=Menu("veggie delight",len(menu_dishes),menu_dishes)
restaurant("Ludhiana Veggie Delight",
           "+91 99999 11111",
           "veggies@abc.com",
           "Krishna Nagar", 
           4.5,
           menu)
restaurant.show()

        """