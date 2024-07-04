"""
    MULTI VALUE CONTAINER

    sequence:
    tuple
    list
    string

    set
    dictionary

    properties:
    1.indexing
    2. begative indexing
    3.slicing
    4.concatination
    5. multiplicity
    6. membership testing
   
"""

#1D list
#indexing 
#      0 1 2
#     -3 -2 -1
my_data=[10,20,30]

numbers=[
    [10,20,30],
    [30,40,50],
    [40,50,60] 
]

large_data=[
    [[10,20,30],
    [30,40,50],
    [40,50,60]],
    [ [10,45,30],
    [40,40,50],
    [40,50,65]]
]

print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(large_data[0])
print(large_data[1][0][0])
print(len(large_data))

name="""john cafe
welcome to cafeteria
todays menu:
black tea
cold coffee"""

print(name[0])
print(name[-1])
print(len(name))

#slicing
data=list(range(10,101,10))
print("data is: ")
print(data)

print("data[0:3]",data[0:3])
print("data[5:7]",data[5:7])
print("data[5:]",data[5:])
print("data[:4]",data[:4])
print("data[-5:-2]",data[-5:-2])

email="swastikverma@gmail.com"
print("email[-1:-4]",email[-1:-4])
print("email[12:]",email[12:])

data1=[10,30,50]
data2=[40,60,80]
data3=data1+data2
print(data3)

data4=data1*2
print(data4)

prices=[100,200,300,500]
#membership testing
print(10 in prices)
print(10 not in prices)

#membership testing on set
set1={"piyush","swastik"}
set2={"devansh","amanpreet"}

print("devansh" in set2)
dict={"student":100,"teacher":32,"shoes":150,"address":"abc"}
# membership testing work on the keys in case of dictionaries
print("teacher" in dict)
print("shoes" in dict)



