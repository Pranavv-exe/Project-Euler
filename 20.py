# sum of the digits in the number 100!
import math    
n=math.factorial(100)
sum=0
while n>0:
  sum+=n%10
  n=n//10
print(sum)
