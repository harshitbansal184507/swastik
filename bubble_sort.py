list=[]
n=int(input("enter number of elements of list: "))
print("enter elements of list: ")
for idx in range(0,n):
    element=int(input())
    list.append(element)

temp=0
print("list:",list)
for i in range(0,n):
    for j in range(i,n):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("after sorting: ")
print ("sorted list: ",list)