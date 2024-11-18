# WAP to add the elements whose value is greater than or equal to itself
# i/p:[2,4,6,10,1]
# o/p:[22,20,16,10,23]

l=eval(input("Enter list: "))
res=[]
for i in l:
    sum=0
    for j in l:
        if i<=j:
            sum+=j
    res.append(sum)
print(res,end=" ")
    
    
