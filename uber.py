from session10b import vehicle
from session10c import driver
from session10d import customer
from session11e import ride

print("------welcome to UBER services-----")
print("you want to sign in as a: ")
print("1. customer")
print("2. driver")
choice=int(input("please enter your choice: "))
def switch(choice):
    if choice == 1:
        Customer=customer()
        Customer.add_customer_details()
        Ride=ride()
        Ride.add_ride_details()
        print("so your driver details for your selected ride is: ")
        Driver=driver()
        Ride.show()
    elif choice==2:
        Driver=driver()
        Driver.add_driver_details()
        Customer=customer()
        Ride=ride()
        Ride.show()

switch(choice)
"""
#driver application
Driver=driver()
Driver.add_driver_details()

#customer application
Customer=customer()
Customer.add_customer_details()

#server
Ride=ride()
Ride.add_ride_details()
Ride.link_customer(Customer)
Ride.link_driver(Driver)
print("RIDE BOOKED... ")
Ride.show()
"""
