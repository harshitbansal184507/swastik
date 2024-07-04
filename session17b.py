from session17 import Patient
from session17a import Consultation
from session15a import Database
from tabulate import tabulate

db=Database()
def main():
    print("=========================")
    print(" WELCOME TO DOCTOR's APP ")
    print("=========================")
    while True:
      print("1. Add new patient ")
      print("2. update existing patient ")
      print("3. delete  existing patient ")
      print("4. view patient by Phone ")
      print("5. view patient by PID ")
      print("6.  view all patient ")
      print("7. Add consultation for patient ")
      print("8. veiw all consultation ")
      print("9. veiw  consultation of a patient")
      print("10. veiw  follow ups")

      print("0. to Quit App")

      choice=int(input("enter your choice: "))

      if choice==1:
        patient=Patient()
        patient.add_patient_details()
        sql="insert into patient values(null,'{name}','{phone}','{email}','{dob}','{gender}','{created_on}')".format_map(vars(patient))
        db.write(sql)
        print("patient created...")
    
      elif choice==3:
            pid=int(input("enter patient id: "))
            sql=" delete from patient where pid={}".format(pid)

            ask =input(("are you sure to delete?? (yes/no): "))
            if ask=="yes":
                db.write(sql)
                print("record has been deleted from the table")
            else:
                print("delete operation skipped.. ")

      elif choice==6:
        sql="select * from patient;"
        rows=db.read(sql)

        columns=['pid','name','phone','email','dob','gender','created_on']
        print(tabulate(rows,headers=columns,tablefmt='grid'))
        #for customer in customers:
             # print(customer)
        print("[cms app] records shown from database...")

      elif choice==7:
        consultation=Consultation()
        consultation.add_consultation_details()
        sql="insert into consultation values(null,'{pid}','{remarks}','{medicines}','{next_followup}','{created_on}')".format_map(vars(consultation))
        db.write(sql)
        print("consulation created...")

      elif choice==8:
        sql="select * from consultation;"
        rows=db.read(sql)

        columns=['cid','pid','remarks','medicines','next_followup','created_on']
        print(tabulate(rows,headers=columns,tablefmt='grid'))
        #for customer in customers:
             # print(customer)
        print("[cms app] records shown from database...")

      elif choice==9:
            PID=input("enter patient's ID : ")
            sql="select * from consultation where pid= '{}'".format(PID)
            rows=db.read(sql)

            columns=['cid','pid','remarks','medicines','next_followup','created_on']
            print(tabulate(rows,headers=columns,tablefmt='grid'))
      
      elif choice==10:
            start=input("enter start datetime(yyyy-mm-dd hh:mm:ss) : ")
            end=input("enter start datetime(yyyy-mm-dd hh:mm:ss) : ")
            sql="select * from consultation where next_followup >= '{}' and next_followup < '{}'".format(start,end)
            rows=db.read(sql)

            columns=['cid','pid','remarks','medicines','next_followup','created_on']
            print(tabulate(rows,headers=columns,tablefmt='grid'))



if __name__ == "__main__":
    main()
