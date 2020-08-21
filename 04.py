h1=0                          #h1 would take the highest value  
for i in range(100,1000):
  for j in range(100,1000):
    prdct=i*j                 #bruteforcing product
    n=prdct                   #n holds value of product so as to not lose the original value
    rev=0                     #rev would hold the reverse of the number to check for palindrome 
    while n>0:                
      rev=10*rev+n%10
      n=n//10
    if rev==prdct and rev>h1:
      h1=rev
print(h1)
