"""
Ride:customer [1 to 1], date,time,from_location,to_location,distance,fare,driver[1to1]
1 ride has 1 customer
1 ride has 1 driver

"""
from session10b import vehicle
from session10c import driver
from session10d import customer
class ride:
    def __init__(self,Customer=None,date="20 june",time="11:30",from_location="south city",to_location="civil lines",distance="6.6",fare="200",Driver=None):
        self.Customer=customer()
        self.date=date
        self.time=time
        self.from_location=from_location
        self.to_location=to_location
        self.distance=distance
        self.fare=fare
        self.Driver=driver()
    def add_ride_details(self):
        print("----ENTER RIDE DETAILS----")
        self.from_location=input("please enter from location: ")
        self.to_location=input("please enter to location: ")
    def link_customer(self):
        self.Customer=customer()
        self.Customer.add_customer_details()
    def link_driver(self):
        self.Driver=driver()
        self.Driver.add_driver_details()

    def show(self):
       
        self.Customer.show()
        print("---------------RIDE DETAILS-----------------")
        print("date: ",self.date,"| time: ",self.time)
        print("from_location: ",self.from_location,"| to_location: ",self.to_location)
        print("distance: ",self.distance,"| fare: ",self.fare)
        print("-------------------------------------")
        self.Driver.show()
"""
ride=ride()
ride.add_ride_details()
ride.show()
"""
