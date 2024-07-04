def add(*args):  # args= arguments
    print(args)
    data=list(args)
    print(data)
    print(type(data))
    print(type(args))

add(10,20,39,49,"hi","john","hello")

print("=====================================")
def numbers(**kwargs):  #kwargs= key arguments
    print(kwargs)
    print(type(kwargs))


numbers(a=10 , b=20, c=30)

def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(10,20,39,49,"hi","john","hello",a=10 , b=20, c=30)

# we can write kuchbhi instead of args and kwargs

