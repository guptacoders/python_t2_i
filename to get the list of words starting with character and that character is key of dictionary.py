# WAP to get the list of words starting with character and that character is key of dictionary
# i/p:- s='Dont wait for your feelings to change to take the action.Take the action and your feeling will change'
#  o/p:- {'D':[Dont],'W':['wait','will'],'f':['for','feelings','feeling']}

s='Dont wait for your feelings to change to take the action.Take the action and your feeling will change'
d={}
l=s.split()
for i in l:
    key=i[0]
    if key in d:
        d[key].append(i)
    else:
        d[key]=[i]
print(d)
