# WAP to find list of common unique items from two list
l1=eval(input("Enter list 1: "))
l2=eval(input("Enter list 2: "))
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            if j in l3:
                continue
            else:
                l3.append(j)
        else:
            continue
print(l3)
