#Pythagorean triplet for which a + b + c = 1000.
#values from 1 to 500 have been bruteforced
br=0        #this variable is used to exit out of loops
for a in range(1,500):
  for b in range(1,500):
    for c in range(1,500):
      if a+b+c==1000:
        if a**2 + b**2==c**2:
          print(a*b*c)
          br=1
          break
    if br==1:
      break
  if br==1:
    break
