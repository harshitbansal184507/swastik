file=open("customer.csv","r")
#data=file.read()
lines=file.readlines()
print("file data: ")
print(lines)

for i in range(len(lines)):
    print(lines[i])