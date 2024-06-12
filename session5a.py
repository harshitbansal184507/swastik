instagram_user_name=["john.j","fionna","harry_h","leo.32","ben_a"]
names=["john jackson","fionna flynn","harrison","leonardo","bennete"]

user_name=input("enter your username: ")


#below approach is wrong as it takes alot of coding to do simple task so here loops come into picture
"""
idx=0
if user_name==instagram_user_name[idx]:
    print("name is: ",names[idx])
elif user_name==instagram_user_name[idx+1]:
    print("name is: ",names[idx+3])  
elif user_name==instagram_user_name[idx+1]:
    print("name is: ",names[idx+3])     
elif user_name==instagram_user_name[idx+4]:
    print("name is: ",names[idx+4])  
elif user_name==instagram_user_name[idx+5]:
    print("name is: ",names[idx+5])         
else:
    print("cannot find the user")
"""



#so below approach was with while loop but we can also use for loop for this purpose
"""
idx=0
while idx<len(instagram_user_name):
    if user_name==instagram_user_name[idx]:
        print("name is: ",names[idx])
    idx+=1    
"""

#FOR LOOP

flag=0
for idx in range(0,len(instagram_user_name)): #isx will start from 0 and goes till length of the list
    print("check",user_name,"with",instagram_user_name[idx])
    
    if user_name==instagram_user_name[idx]:
        print("name is: ",names[idx])
        flag=True
        break

if flag ==0:
        print("username does not exist")
