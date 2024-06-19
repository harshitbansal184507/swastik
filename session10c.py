"""
driver:name,phone,email,license_number,rating,gender,age,vehicle[1 to 1]
1 driver has 1 vehicle
"""

from session10b import vehicle

class driver:
    def __init__(self,name="NA",phone="NA",email="NA",license_number="NA",rating="NA",gender="NA",age="NA",vehicle=None):
        self.name=name
        self.phone=phone
        self.email=email
        self.license_number=license_number
        self.rating=rating
        self.gender=gender
        self.age=age
        self.vehicle=vehicle

    def add_driver_details(self):
        print("----ENTER DRIVER DETAILS----")
        self.name=input("enter driver name: ")
        self.phone=input("enter driver phone: ")
        self.email=input("enter driver email: ")
        self.license_number=input("enter driver license number: ")
        self.rating=float(input("enter driver rating: "))
        self.gender=input("enter driver gender: ")
        self.age=int(input("enter driver age: "))
        print("----ENTER VEHICLE DETAILS----")
        self.vehicle=vehicle() # object construction
        self.vehicle.add_vehicle_details()

    def show(self):
        print("---------------DRIVER-----------------")
        print("name: ",self.name,"| phone: ",self.phone)
        print("email: ",self.email,"| lisence number: ",self.license_number)
        print("gender: ",self.gender,"| age: ",self.age)
        print("---------------------------------------")
        self.vehicle.show()

#driver=driver()
#driver.add_driver_details()
#driver.show()