"""
(if the number of rice get double on each box of chess)
1   2    4    8   16   32  .... 64 times
"""
a=1
add=1
print("1 box = 1 ",end=" || ")
for i in range(2,65):
    sum=2*a
    print (i,"box =",sum, end=" || ")
    a=sum
    add=add+sum
print()
print("total pieces of rice on whole chess board are: ",add)

    


