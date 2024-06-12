"""
another brick in the wall
who placed the last brick and how many?
mr. john -> requirement | create a wall with 13 bricks
             
jack: 1 brick lgata hai
joe: 2 times the jack's bricks
                   total bricks
    jack: 1             1
    joe:  2             3

    jack: 2             5
    joe:  4             9

    jack: 3             12 
    joe:  6             13

    (joe-> last brick)
    ( 1 brick at last)
 (basicaa;y, we have to find out that who placed the last brick and how many bricks did he placed at last)   
"""
bricks=int(input("enter the number of bricks: "))
n=0
jack=0
joe=0
total_bricks=0
temp=0
while(total_bricks<bricks+1):
    jack+=1
    print("jack:",jack)
    total_bricks+=jack
    print("bricks: ",total_bricks)
    n+=1
    if(total_bricks<bricks+1):
       joe=jack*2
       print("joe: ",joe)   
       total_bricks+=joe
       print("bricks: ",total_bricks)
       n+=1
        
if(total_bricks>bricks):
    temp=total_bricks-bricks
    total_bricks=bricks
print("but total number of bricks placed should be ",total_bricks,"so...")
19
if(n%2==0):
    print("the last brick was placed by joe")
    joe=joe-temp
    print("he placed ",joe ," bricks at last")
else:
    print("the last brick was placed by jack")
    jack=jack-temp
    print("he placed ",jack ," bricks at last") 




