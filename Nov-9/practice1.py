# WAP to check whether the String is balanced or not 
# All the elements of second String should be in first String

s1=input("Enter String 1: ")
s2=input("Enter String 2: ")
flag=0
for i in s2:
    if i in s1:
      continue
    else:
      flag=1
if(flag==1):
  print("String is not balanced")
else:
  print("String is balanced")
       