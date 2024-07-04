"""
FILE OPERATIONS
"""
quote=input("enter data that you want to write in file: ")
quote1="search the candle rather than cursing the darkness\n"
quote2="be exceptional\n"

#file=open("quotes.txt","w")
file=open("quotes.txt","a")

file.write(quote)
file.write(quote1)
file.write(quote2)

#free memory resources once, you have used file
file.close()
print("data written...")