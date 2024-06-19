"""
  code 3 objects:
  1.dish: name , price , rating
  2.menu: name , number of dishes , dishes  
    | 1 menu can have many dishes(1 to many)
  3.restaurent: name , phone email , addres , operating_hours , ratings , menu 
    | 1 restaurent can have 1 menu(1 to 1)
"""
#class for the object dish
class dish:
    #parametrized constructors, with default value of arguments passed to it
    def __init__( self,  name="NA", price=0 , rating=1.5):
        self.name=name
        self.price=price
        self.rating=rating

    def show(self):
        print("-------------------------------------------")
        print("dish: ",self.name," | ",self.price," | ",self.rating)
        print("-------------------------------------------")

#dish1=dish("pizza",120,4.5)
#dish2=dish("pasta",60,4)
#dish3=dish()
"""
dish1.show()
dish2.show()
dish3.show()
"""
#dishes=[dish1,dish2,dish3]
"""
dishes=[
    dish(),
    dish("pizza",120,4.5),
    dish("pasta",60,4)
]
print("dishes are:")
for idx in range (len(dishes)):
    dishes[idx].show() """