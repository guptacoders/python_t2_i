# WAP to convert Roman Numbers to Integer [From 1 to 1000 only]
s=input("Enter Roman Number: ")
roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
i=0
n=0
while i<len(s):
    if i+1<len(s) and s[i:i+2] in roman:
        n+=roman[s[i:i+2]]
        i+=2
    else:
        n+=roman[s[i]]
        i+=1
print(n)
