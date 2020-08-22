#Counting Sundays that fell on the first of the month during the twentieth century(1 jan 1901 to 31 dec 2000)


dy=2          #this variable holds value of days of the week(dy%7 would correspond to the day of the week where 0 is sunday, 1 is monday and so on)     
count=0       #hold value of the number of sundays that were on the first day of the month
y=1901        #holds value of the year
while True:
  m=1         #holds value of the month number(1 being january and so on)
  if y==2001:
    break
  if (y%4==0 and y%100!=0) or (y%400==0) :     #condition for leap year
    while m<13:
      if dy%7==0:
        count+=1
      if m in [1,3,5,7,8,10,12]:
        dy+=3                                  #since they have 4 weeks and 3 extra days
      elif m==2:
        dy+=1                                  #since they have 4 weeks and 1 extra day
      else:
        dy+=2                                  #since they have 4 weeks and 1 extra day
      m+=1
     
  else:
    while m<13:
      if dy%7==0:
        count+=1
      if m in [1,3,5,7,8,10,12]:
        dy+=3                                 #since they have 4 weeks and 3 extra days
      elif m==2:
        dy+=0                         
      else:
        dy+=2
      m+=1                                   #since they have 4 weeks and 1 extra day
  y=y+1
print(count)
