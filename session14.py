import mysql.connector as db
from session13 import Customer
#database username and password
"""
username="root"
password="swastik.."

host="192.168.196.143"
database="python"
"""
connection = db.connect(user="root",
                      password="swastik..",
                      host="127.0.0.1",
                      database="python",)

print("connection created.")
print(connection)
"""
customer=Customer()
customer.add_customer_details()
"""
#sql="insert into customer values(null,'diksha','91+ 99999 11111','diksha@example.com',25,'female');"

#sql="insert into Customer values(null,'{}','{}','{}',{},'{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)
#sql="update customer set name='johnnathon' where cid=5;"
#sql="delete from customer where cid=5;"
sql="drop table customer;"
cursor=connection.cursor()
cursor.execute(sql)
connection.commit()

print("sql statement executed...")