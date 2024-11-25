#  QB-460
# Simple Encryption

#  i/p:- s='This is python'
#  shift key=4
#  o/p:- T pohiynists h


s=input("Enter Input: ")
k=int(input("Enter Shift key: "))
s1=''
for i in range(k):
    s1+=s[i::k]
print(s1)
