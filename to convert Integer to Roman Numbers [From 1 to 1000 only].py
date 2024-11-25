# WAP to convert Integer to Roman Numbers [From 1 to 1000 only]
n=int(input("Enter Number"))
val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
r=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
roman=""
i=0
while n>0:
    for j in range(n//val[i]):
        roman+=r[i]
        n-=val[i]
    i+=1
print(roman)
