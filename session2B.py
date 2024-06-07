#dictionary-
# dictionaries are the last and most important multi value container

friends={"s":"swastik","a":"amanpreet","p":"piyush"}
print(friends,type(friends),id(friends))
print(friends["a"])

#we can write abything in place of values it can either be set,lists,tuple,dictionaries
instagram={
    "swastik":{1:"amanpreet",2:"anmol",3:"rishi",4:"piyush"},
    "amanpreet":{"swastik","piyush","devansh"},
    "devansh":{"swastik","amanpreet","piyush"}
}
print(instagram["swastik"])
print(instagram["amanpreet"])
print(instagram["swastik"][1])
print(instagram["amanpreet"] & instagram["devansh"])