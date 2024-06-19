"""
driver has a vehicle
customer can book a ride
identify objects with attributes

vehicle: reg_number,brand,model,color
driver:name,phone,email,license_number,rating,gender,age,vehicle[1 to 1]
1 driver has 1 vehicle
customer:name,phone,email,address,gender,age
Ride:customer [1 to 1], date,time,from_location,to_location,distance,fare,driver[1to1]
1 ride has 1 customer
1 ride has 1 driver

"""
class vehicle:
    def  __init__(self,reg_number="NA",brand="NA",model="NA",color="white"):
        self.reg_number=reg_number
        self.brand=brand
        self.model=model
        self.color=color

    def add_vehicle_details(self):
        self.reg_number=input("eneter vehicle number: ")
        self.brand=input("enter brand of the vehicle: ")
        self.model=input("enter model of the vehicle: ")
        self.color=input("enter color of the vehicle: ")

    def show(self):
        print("---------------VEHICLE-----------------")
        print("number: ",self.reg_number,"| brand: ",self.brand)
        print("model: ",self.model,"| color: ",self.color)
        print("---------------------------------------")


#vehicle=vehicle("PB10AB100","TVS","swift","black")
#vehicle=vehicle()
#vehicle.add_vehicle_details()
#vehicle.show()