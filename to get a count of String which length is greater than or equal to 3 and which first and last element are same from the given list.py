# WAP to get a count of String which length is greater than or equal to 3
# and which first and last element are same from the given list
l=['abc','aba','1221','xyzx','12345']
count=0
for i in l:
    if len(i)>=3:
        if i[0]==i[-1]:
            count+=1
print(count)

#          OR
# s=list(filter(lambda i:i[0]==i[-1],l))
# print(len(s))
