a1=1  #first term
a2=2  #second term
a3=0  #third term
sum=0
while a3<4000000:
  a3=a1+a2    
  if a3%2==0:
    sum=sum+a3
  a1=a2   
  a2=a3
print(sum+2) #2 is added since it is is the fixed term and not itrated in the loop
