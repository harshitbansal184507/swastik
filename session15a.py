# database oops
import mysql.connector as db


class Database:
    def __init__(self):
        self.connection = db.connect(user="root",
                      password="swastik..",
                      host="127.0.0.1",
                      database="python",)
        

        self.cursor=self.connection.cursor()

        print("[database] connection created.")
        
    
    #insert/update/delete in db
    def write(self,sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("[database] sql statement: ",sql," \nexecuted successfully...")
        #customer=Customer()
        #customer.add_customer_details()

    
    #fetch data from db
    def read(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        
        return result
