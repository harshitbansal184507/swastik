#bitwise operator
#&,|,^
num1=10
num2=8
print("num1 in binary is: ",bin(num1))
print("num2 in binary is: ",bin(num2))
result1=num1&num2 
result2=num1|num2
result3=num1^num2
#^ : exclusive or means one should be 0 and one should 1 then the result will be 1
print("result1: ",result1)
print("result1: ",result1)
print("result1: ",result1)

#shift operators
#>>,<<
num1=8
num2=3
result4=num1>>num2# 8//2 power3   #(num1 // 2 power num2)
print("result of right shift is:",result4)
# in right shift number will get divide by 2**3
result5=num1<<num2# 8* 2power3   #(num1 * 2 power num2)
print("result of left shift is:",result5)
# in left shift we will multiply the number by 2**3
 
 #base will always be 2 because because we r talking about binary numbers
number=11
result= number>>2
print(result)

#11
#0 0 0 0 1 0 1 1 
# >> 2
# _ _ 0 0 0 0 1 0 ->2

#-11
#0 0 0 0 1 0 1 1
#1 1 1 1 0 1 0 0
#              1 
#1 1 1 1 0 1 0 1
# >>2
#_ _ 1 1 1 1 0 1
#1 1 1 1 1 1 0 1 
#0 0 0 0 0 0 1 0
#              1
#0 0 0 0 0 0 1 1 ->-3

#-13
#0 0 0 0 1 1 0 1
#1 1 1 1 0 0 1 0 (1's compliment)
#              1
#1 1 1 1 0 0 1 1 (2's compliment)
# >>2
#_ _ 1 1 1 1 0 0 
#1 1 1 1 1 1 0 0 (added 1 1 for -ve sign)
#0 0 0 0 0 0 1 1 (1's compliment)
#              1 (2's compliment)
#0 0 0 0 0 1 0 0->-4 