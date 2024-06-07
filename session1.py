# first program

#create statement-> you are creating a single value container in RAM
#user_name is a REFERENCE VARIABLE
user_name="auribises"

#read statement->  to read  data inside a container
print(user_name, id(user_name))

#update statement
user_name="swastik"
print(user_name, id(user_name), type(user_name))
#we can use type or class to get the datatype of the data

user_name=1001
print(user_name, id(user_name), type(user_name))

#delete statement
del user_name
print(user_name)
# so the variable user_name gets deleted and it will show us an error that user_name is not defined




