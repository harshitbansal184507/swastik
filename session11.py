from session10d import customer


print("-------------------------------------")
print("welcome to customer management system")
print("-------------------------------------")



while True:
    print("1. add customer:")
    print("2. view customer:")
    print("0. exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        file=open("customer.csv","a")
        Customer = customer()
        Customer.add_customer_details()
        Customer.show()

        Data=Customer.to_csv()
        file.write(Data)
        print("data written: ",Data)

    elif choice==2:
        file=open("customer.csv","r")
        lines=file.readlines()
        for line in line:
            print(line)

    elif choice==0:
        print("-------------------------------------")
        print("thanyou for using customer service")
        print("-------------------------------------")
        break
    
