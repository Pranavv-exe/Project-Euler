s1=0  #sum of the squares
s2=0  #square of the sum
s=0   #sum of natural numbers
for i in range(1,101):
  s1=s1+i**2

for j in range(1,101):
  s=s+j
  s2=s**2

print(s2-s1)
