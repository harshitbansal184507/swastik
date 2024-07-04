"""
doctor's app

user is a doctor
doctor should be able to add patients
doctor should be able to add consultations of the customer

docotr -> user of a application
patient: pid,name,phone,email,dob,gender,created_on
consultation: cid,pid,remarks,medicines,next_followup,created_on
"""

import datetime
"""
 create table patient(
       pid int primary key auto_increment,
       name varchar(60),
       phone varchar (20),
       email varchar(256),
       dob date,
       gender varchar(256),
       created_on datetime)
"""
class Patient:
    def __init__(self,pid=0,name="NA",phone="",email="",dob="",gender=""):
        self.pid=pid
        self.name=name
        self.phone=phone
        self.email=email
        self.dob=dob
        self.gender=gender
        self.created_on=datetime.datetime.now()

    def add_patient_details(self):
        print("----ENTER PATIENT DETAILS____")
        self.name=input("enter patient name: ")
        self.phone=input("enter patient phone: ")
        self.email=input("enter patient email: ")
        self.dob=input("enter patient DOB(yyyy-mm-dd): ")
        self.gender=input("enter patient gender: ")

    def show(self):
        print("=======PATIENT========")

        patient = """
        | {pid} | {name} | {phone} |
        | {email} | {age} |  
        | {gender} | {created_on} |     
        """.format_map(vars(self))

        print(patient)
        print("=======================")