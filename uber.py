"""
Ride:customer [1 to 1], date,time,from_location,to_location,distance,fare,driver[1to1]
1 ride has 1 customer
1 ride has 1 driver

"""
from session10b import vehicle
from session10c import driver
from session10d import customer

class ride:
    def __init__(self,customer=None,date="NA",time="NA",from_location="NA",to_location="NA",distance="NA",fare="NA",driver=None):
        self.customer=customer
        self.date=date
        self.time=time
        self.from_location=from_location
        self.to_location=to_location
        self.distance=distance
        self.fare=fare
        self.driver=driver

    def add_ride_details(self):
        self.customer=customer()
        self.customer.add_customer_details()
        print("----ENTER RIDE DETAILS----")
        self.date=input("please enter date: ")
        self.time=input("please enter time: ")
        self.from_location=input("please enter from location: ")
        self.to_location=input("please enter to location: ")
        self.distance=input("please enter distance: ")
        self.fare=input("please enter fare: ")
        self.driver=driver()
        self.driver.add_driver_details()

    def show(self):
        
        self.customer.show()
        print("---------------RIDE-----------------")
        print("date: ",self.date,"| time: ",self.time)
        print("from_location: ",self.from_location,"| to_location: ",self.to_location)
        print("distance: ",self.distance,"| fare: ",self.fare)
        print("---------------------------------------")
        self.driver.show()

ride=ride()
ride.add_ride_details()
ride.show()
