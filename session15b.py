# customer management app
import mysql.connector as db

from session15a import Database
from session15 import Customer
from tabulate import tabulate

def main():
    print("------------------")
    print("WELCOME TO CMS APP")
    print("------------------")

    while True:
        print("1. Add new customer ")
        print("2. update existing customer ")
        print("3. delete  existing customer ")
        print("4. view customer by Phone ")
        print("5. view customer by CID ")
        print("6.  view all customer ")
        print("0. to Quit App")

        choice=int(input("enter your choice: "))
        db=Database()
        if choice==1:
            customer=Customer()
            customer.add_customer_details()
            sql="insert into Customer values(null,'{}','{}','{}',{},'{}','{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender,customer.created_on)
            print("sql statement executed...")
            db.write(sql)
            print("[CMS app] ",customer.name," has been added to the database...")
            
        elif choice==2:
            CID=input("enter customer's ID whose data you want to update : ")
            sql="select * from customer where cid= '{}'".format(CID)
            rows=db.read(sql)
            print(rows)
            customer=Customer(cid=rows[0][0],name=rows[0][1],phone=rows[0][2],email=rows[0][3],age=rows[0][4],gender=rows[0][5],)
            
            print("customer to update: ")
            customer.show()
            customer.update_customer_details()

            sql="update customer set name='{name}' ,phone='{phone}',email='{email}',age='{age}',gender='{gender}',created_on='{created_on}' where cid='{cid}'".format_map(vars(customer))
            db.write(sql)
            customer.show()
           
        elif choice==3:
            cid=int(input("enter customer id: "))
            sql=" delete from customer where cid={}".format(cid)

            ask =input(("are you sure to delete?? (yes/no): "))
            if ask=="yes":
                db.write(sql)
                print("record has been deleted from the table")
            else:
                print("delete operation skipped.. ")
        elif choice==4:
            phone=input("enter customer's phone number: ")
            sql="select * from customer where phone= '{}'".format(phone)
            rows=db.read(sql)

            columns=['cid','name','phone','email','age','gender','created_on']
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            #for customer in customers:
        elif choice==5:
            CID=input("enter customer's ID : ")
            sql="select * from customer where cid= '{}'".format(CID)
            rows=db.read(sql)

            columns=['cid','name','phone','email','age','gender','created_on']
            print(tabulate(rows,headers=columns,tablefmt='grid'))
        elif choice==6:
            sql="select * from customer;"
            rows=db.read(sql)

            columns=['cid','name','phone','email','age','gender','created_on']
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            #for customer in customers:
               # print(customer)
            print("[cms app] records shown from database...")
        elif choice==0:
            break
        else:
            print("[CMS app] invalid choice")

if __name__ == "__main__":
    main()
