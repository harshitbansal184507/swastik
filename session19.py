numbers=list(range(10,101,10))
print("numbers is: ",numbers)
print("numbers type is: ",type(numbers))

#append means add in the end
numbers.append(99)
numbers.append(75)
numbers.append(130)
numbers.append(11)

#built in functions
print("numbers is: ",numbers)
print("len is:",len(numbers))
print("sum is:",sum(numbers))
print("min is:",min(numbers))
print("max is:",max(numbers))
print("avg is:",sum(numbers)/len(numbers))

result=list(reversed(numbers))
print("result after reversing is: ",result)

#hw: reverse the below list 
data=[10,20,30,40,50]
data1=[]
"""
for idx in range(len(data)-1,-1,-1):
    data1.append(data[idx])

print(data1)
   """

mid=int(len(data)/2)
print("mid is",mid)
for i in range(0,mid): 
    print(data[i])


idx=data.index(40)
print("idx is: ",idx)
result=data.count(30)
print("result is: ",result)

data=[10,20,30,0,5,90,46]
names=["swastik","aman","piyush","devansh","john"]
data.sort()
print("data is: ",data)
names.sort()
print(names)
print(max(names))
print(min(names))
names.remove("john")
data.remove(0)
print("new data is: ",data)
print("new names are: ",names)

#pop means get the last element out
data=[10,20,30,40,50]
data.pop()
print("data after pop: ",data)
data.pop(0) #means pop the element at index 0
data.clear()#will remove all the elements

data=[10,20,30,40,50]
data.append(99) #append insert element at last
data.insert(2,77) # insert add data at the given index
data.insert(-1,88)
print(data)