#sum of the digits of the number 2^1000
n=2**1000 #16
sum=0
while n>0:
  sum=sum+n%10
  n=n//10
print(sum)
