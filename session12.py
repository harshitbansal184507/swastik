#dish=name,price,rating

class Dish:
    def __init__(self,name="NA",price=0,rating=4.5):
        self.rating=rating
        self.name=name
        self.price=price

    def show(self):
        print("-------------------------DISH-----------------------")
        print("name: ",self.name,"| price: ",self.price,"| rating: ",self.rating)
        print("----------------------------------------------------")

    


#list of dish objects
dishes=[Dish("dal makhani", 150 , 4.5),Dish("shahi paneer", 250 , 5),Dish("mix veg", 200 , 4),Dish("burger ", 50 , 4.5),Dish("noodles ", 100 , 4),Dish("spring roll", 170 , 5)]


def bubble_sort(dishes):
        for i in range(0,len(dishes)):
            for j in range(i,len(dishes)):
                if dishes[i].price>dishes[j].price:
                    dishes[i],dishes[j]=dishes[j],dishes[i]

#for idx in range(len(dishes)):
#    dishes[idx].show()
dish=Dish()
for dish in dishes:
    dish.show()
bubble_sort(dishes)
print("AFTER SORTING WRT PRICE: ")
for dish in dishes:
    dish.show()
