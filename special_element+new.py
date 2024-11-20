# WAP to entered string by user create a dictionary which key is starting character of word and value is how many times it comes
# i/p: s="asd bsg asp bcv cdv asg"
# o/p: {'a':5,'b':2,'c':1}
#                 &
#     {'a':['asd','asp','asg'], 'b':['bsg','bcv'],'c':['cdv']}

s="asd bsg asp bcv cdv asg"
spl=s.split(" ")
d={}
d1={}
for i in spl:
    d[i[0]]=d.get(i[0],0)+1
print(d)

for i in spl:
    if i[0] not in d1:
        d1[i[0]]=[]
        d1[i[0]].append(i)
    else:
        d1[i[0]].append(i)
print(d1)
