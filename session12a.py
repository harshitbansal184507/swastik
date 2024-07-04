"""
customer:
dishes:
order:

1 customer can place many orders
1 order can have many dishes
"""
from session12  import Dish

class Customer:
    def __init__(self,name="NA",phone=0,email="NA",address="NA"):
        self.address=address
        self.name=name
        self.email=email
        self.phone=phone
    
    def show(self):
        print("-------------------------DISH-----------------------")
        print("name: ",self.name,"| phone: ",self.phone)
        print("address: ",self.address,"| email: " ,self.email)
        print("----------------------------------------------------")