numbers = {10,20,11,22,55,57,11}
#{} refers to a set which do not supports duplicacy
numbers1 = [10,20,11,22,55,57,11]
#where as [] refers to list which supports duplicacy
print(numbers,type(numbers),id(numbers))
print(numbers1,type(numbers1),id(numbers1))

john_friends={"joe","jim","fionna","harry","kim","joe"}
sia_friends={"joe","george","leo","jack","ben"}
print(john_friends)
print(sia_friends)

mutual_friends=john_friends & sia_friends
print(mutual_friends)


