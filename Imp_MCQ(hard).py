l1=["A","B","C","D","E"]
l2=l1.copy()
l3=l1[::-1]
l2[4]="G"
l3[3]="H"
l1[4]=l2[4]
l1[3]=l3[3]
s=0
for i in(l1,l2,l3):
    if i[4]=="G":
        s+=7
    if i[3]=="H":
        s+=22
    if i[2]=="C":
        s+=30
print(s)
