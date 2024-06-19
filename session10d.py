"""
customer:name,phone,email,address,gender,age

"""

class customer:
    def  __init__(self,name="NA",phone="NA",email="NA",address="NA",gender="NA",age="NA"):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.gender=gender
        self.age=age


    def add_customer_details(self):
        print("----ENTER CUSTOMER DETAILS----")
        self.name=input("enter customer name: ")
        self.phone=input("enter customer phone: ")
        self.email=input("enter customer email: ")
        self.address=input("enter customer address: ")
        self.gender=input("enter customer gender: ")
        self.age=input("enter customer age: ")

    def show(self):
        print("---------------CUSTOMER-----------------")
        print("name: ",self.name,"| phone: ",self.phone)
        print("email: ",self.email,"| address: ",self.address)
        print("gender: ",self.gender,"| age: ",self.age)
        print("---------------------------------------")

#customer=customer()
#customer.add_customer_details()
#customer.show()