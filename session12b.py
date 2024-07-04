from session12a import Customer
from session12 import Dish

class order:
    def __init__(self,oid=0,dishes=None,customer=None,total=0):
        self.oid=oid
        self.dishes=dishes
        self.customer=Customer()
        self.total=total
    
    def show(self):
        print("-------------------------DISH-----------------------")
        print("oid: ",self.oid,"| total: ",self.total)
        print("----------------------------------------------------")

        print("ORDER PLACED BY: ")
        self.customer.show()

        print("--------------------Order Dishes--------------------")
        for dish in self.dishes:
             dish.show()
        print("----------------------------------------------------")

    def link_dishes(self, dishes):
        self.dishes = dishes

        for dish in self.dishes:
            self.total += dish.price
            
    def link_customer(self, customer):
        self.customer = customer
