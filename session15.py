"""
    create table customer(   
    cid int primary key auto_increment,
    name varchar(90),
    phone varchar(15),
    email varchar (70),
    age int,
    gender varchar(20),
    created_on datetime
    );
"""
import datetime
class Customer:
    def __init__(self,cid=0,name="NA",phone="NA",email="NA",age=0,gender="NA",created_on=""):
        self.cid=cid
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()
    def add_customer_details(self):
        print("----ENTER CUSTOMER DETAILS____")
        self.name=input("enter your name: ")
        self.phone=input("enter your phone: ")
        self.email=input("enter your email: ")
        self.age=input("enter your age: ")
        self.gender=input("enter your gender: ")
        #we will not get input for created on
        #created_on is a system date time stamp
    def update_customer_details(self):
        name=input("enter your name: ")
        if len(name)!=0:
            self.name=name
        phone=input("enter your phone: ")
        if len(phone)!=0:
            self.phone=phone
        email=input("enter your email: ")
        if len(email)!=0:
            self.email=email
        age=input("enter your age: ")
        if len(age)!=0:
            self.age=age
        gender=input("enter your gender: ")
        if len(gender)!=0:
            self.gender=gender
    
    def show(self):
        print("---------------------CUSTOMER-------------------")
        print("| {} | {} | {} |".format(self.cid,self.name,self.phone))
        print("| {} | {} | {} |".format(self.email,self.age,self.gender))
        print("| {} |".format(self.created_on))
        print("-------------------------------------------------")