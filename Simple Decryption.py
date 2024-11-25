# Simple Decryption

#  i/p:- T pohiynists h
#  o/p:- s='This is python'
#  shift key=4

s = input("Enter Transformed Input: ")
k = int(input("Enter Shift key: "))
n = len(s)
result = [''] * n  # Empty list to hold the reconstructed string

# Distribute characters from 's' into 'result' based on the key
index = 0
for i in range(k):
    for j in range(i, n, k):
        result[j] = s[index]
        index += 1
# Join and print the reconstructed string
decrypted = ''.join(result)
print("Original String: ", decrypted)
