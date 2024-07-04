name=input("enter customer name: ")
phone=input("enter customer phone: ")
email=input("enter customer email: ")
customer_details="{},{},{}\n".format(name,phone,email)

file=open("customer.csv","a")
file.write(customer_details)

print("customer data saved...")
file.close()