#loop would begin from 4
count=2       #count is 2 for '2' and '3' since loop begins form 4
a=4     
while count<10001:
  for i in range(2,int(a/2)+1):
    if a%i==0:
      break
  else:
    count+=1
  a+=1
print(a-1)    #one is subracted since it adds extra one at the end of last while loop
    
    
