#Kimora Lee
#03-15-2024
#P3LAB
#Assignment tests student's knowledge of how to write code that displays information to users

year = int(input())

if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print(year, "- leap year")
       else:
           print(year, "- not a leap year")
   else:
       print(year, "- leap year")
else:
   print(year, "- not a leap year")

