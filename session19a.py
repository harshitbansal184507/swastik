#explore SET
#unique

john_followers={"fionna","sia","jack","john","george"}
print(john_followers)
print(type(john_followers))
print(len(john_followers))

numbers=list(range(10,101,10))
numbers1=set(numbers)
print(numbers)
print(numbers1)

numbers1.add(101)
numbers1.add(201)
numbers1.add(301)
print("numbers1 is: ",numbers1)
#numbers1.pop()
#numbers1.pop()
#print(numbers1)
numbers1.remove(301)
numbers1.remove(30)
numbers1.remove(90)
numbers1.discard(201)
#discard is only available in set
print("after removing numbers1 is: ",numbers1)

john_followers={"fionna","sia","joe","jack","john","george"}
jack_followers={"anna","sia","kia"}
fionna_followers={"sia","joe"}

mutual_followers=john_followers.intersection(jack_followers)
print(mutual_followers)
result=fionna_followers.issubset(john_followers)
print("result is: ",result)

a={1,2,3,4,5}
b={4,5,6,7,8}
"""
+ operation will not work on sets
c=a+b
print("c is: ",c)
"""
d=a-b
print("d is: ",d)
e=a^b # common elements minus krdo
print("e is: ",e)
f=a|b # union function
print("f is: ",f)
a.clear()
print("a is",a)
print(len(a))

#create an empty set
my_set=set()