#Collatz Problem where,
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

h=0           #holds the value of the higest chain
a=0           #holds vaue of the number which produces the highest chain
for i in range(2,1000000):
  j=i         #j holds current value of i so as to not lose the original value of i during calculations
  count=0     #this variable counts number of iterations
  while i!=1:
    if i%2==0:
      i=i/2
      count+=1
    else:
      i=3*i+1
      count+=1
  if count>h:
    h=count
    a=j
print(a,"produces the longest chain with",h,"iterations")
