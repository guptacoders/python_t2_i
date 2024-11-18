# WAP for a given list l of size n . You need to count the number of special elements
# in the given list and  element is special if removal of that element makes the list balanced
# The list will be balanced if the sum of even index element = the sum of odd index element.
# Also print the updated list after removal of special element.
# i/p: [2,1,6,4]
# odd index ele= 2+6=8 is not equal to 1+4=5 make it balance ,  updated:[2,6,4], no.of special ele=1
# o/p: No.of special element=1 and  [2,6,4]

l=eval(input("Enter list 1: "))
cn=0
    
for i in range(0,len(l)):
    c=l.copy()
    c.pop(i)
    sum1=sum(c[0::2])   
    sum2=sum(c[1::2])
    if sum1==sum2:
        cn+=1
        print("updated list:",l[0:i]+l[i+1:])
print("No of special element=",cn)
