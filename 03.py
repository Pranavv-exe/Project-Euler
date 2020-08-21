n=600851475143
fac=2         #its initial value is 2 since 2 is lowest prime number
count=0
x=2           #x will take all the bruteforcing values
while x<=n:
  if n%x==0:
    while n%x==0:
      n=n/x
    fac=x
  x=x+1

print(fac)
