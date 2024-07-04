"""
  1. execute mysql commands

    object relational mapping(ORM)
    
    create database python
    use python

    create table Customer(
    cid int primary key auto_increment,
    name varchar(90),
    phone varchar(15),
    email varchar (70),
    age int,
    gender varchar(20)
    );
    
    insert into customer values(null,'john','91+ 99999 22222','john@example.com',20,'male');
    insert into customer values(null,'fiona','91+ 99999 55555','fiona@example.com',25,'female');

    select*from customer;
    select* from customer where cid=2;
    select name,phone from customer where cid=2;

    update customer set name='johnnathon' where cid=1;
    delete from customer where cid=1;

    create table Address(
    aid int primary key auto_increment,
    houseno varchar(90),
    adressline1 varchar(15),
    addressline2 varchar (70),
    city varchar(90),
    state varchar(20),
    zipcode varchar(90),
    landmark varchar(80)
    );
  2. work with virtual
  3. installation of driver
  4. sql connection with python

  customer: name,phone,email,age
  address: houseno,addressline1,addressline2,city state zipcode,landmark
  """

class Customer:
    def __init__(self,cid=0,name="NA",phone="NA",email="NA",age=10,gender="NA"):
        self.cid=cid
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
    def add_customer_details(self):
        print("----ENTER CUSTOMER DETAILS____")
        self.name=input("enter your name: ")
        self.phone=input("enter your phone: ")
        self.email=input("enter your email: ")
        self.age=input("enter your age: ")
        self.gender=input("enter your gender: ")

    def show(self):
        print("---------------------CUSTOMER-------------------")
        print("| {} | {} | {} |".format(self.cid,self.name,self.phone))
        print("| {} | {} | {} |".format(self.email,self.age,self.gender))
class Address:
    def __init__(self,aid=0,houseno="NA",addressline1="NA",addressline2="NA",city=10,state="NA",zipcode="NA",landmark="NA"):
        self.aid=aid
        self.houseno=houseno
        self.addressline1=addressline1
        self.addressline2=addressline2
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.landmark=landmark
       
customer1=Customer(1,'john','91+ 99999 22222','john@example.com',20,'male')
customer1.show()