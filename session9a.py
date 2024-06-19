"""
  code 3 objects:
  1.dish: name , price , rating
  2.menu: name , number of dishes , dishes  
    | 1 menu can have many dishes(1 to many)
  3.restaurent: name , phone email , addres , operating_hours , ratings , menu 
    | 1 restaurent can have 1 menu(1 to 1)
"""
from session9 import dish

class Menu:
  #parametrized constructors, with default value of arguments passed to it
    def __init__( self,  name="NA", number_of_dishes=0,menu_dishes=[]):
        self.name=name
        self.number_of_dishes=number_of_dishes
        self.menu_dishes=menu_dishes


    def show(self):
        print("-------------------------------------------")
        print("MENU: ",self.name," | ",self.number_of_dishes)
        print("-------------------------------------------")
        print("dishes are:")
        for idx in range(len(self.menu_dishes)):
          self.menu_dishes[idx].show()

"""
dishes=[dish(),dish("dal makahani",250,5),dish("paneer masala",500,4.5)]
Menu=Menu("Indian veggie delight",3,dishes)

Menu.show()"""