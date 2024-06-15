"""
numbers=[1,3,5]

max=numbers[0]
for idx in range(0,len(numbers)):
    if numbers[idx]>max:
        max=numbers[idx]

print("max is: ",max)
"""

def get_max(data,length):
    if length==1:
        return data[0]
    else:
        previous = get_max(data,length-1)
        current = data[length-1]

        if previous > current:
            return previous
        else:
            return current
    
numbers=[10,20]
max=get_max(numbers,len(numbers))
print("result is:",max)