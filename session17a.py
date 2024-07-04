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
    create table consultation(
    cid int primary key auto_increment,
    pid int,
    remarks varchar (256),
    medicines varchar(256),
    next_followup datetime,
    created_on datetime,
    FOREIGN KEY (pid) REFERENCES Patient (pid)
    )"""

class Consultation:
    def __init__ (self,cid=0,pid=0,remarks="",medicines="",next_followup="",created_on="" ):
        self.cid=cid
        self.pid=pid
        self.remarks=remarks
        self.medicines=medicines
        self.next_followup=next_followup
        self.created_on=datetime.datetime.now()

    def add_consultation_details(self):
        print("----ENTER PATIENT DETAILS____")
        self.pid=input("enter patient ID: ")
        self.remarks=input("enter patient remarks: ")
        self.medicines=input("enter medicines: ")
        self.next_followup=input("enter next_followup (yyyy-mm-dd hh:mm:ss): ")

    def show(self):
        print("=======CONSULTATION========")

        consultation = """
        | {pid} | {name} | {phone} |
        | {email} | {age} |  
        | {gender} | {created_on} |     
        """.format_map(vars(self))

        print(consultation)
        print("============================")