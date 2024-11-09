import string


print('Delhi'+''+'Abd')
print('Abd'*3)

S='python'
print('p' in S)
print('p' not in S)


print('Hi' and 'Hello')
print('Hi' or 'Hello')
print(''and 'Hi')
print(''or 'Hi')
print('Hi' and '')

#MCQ's
print(ord("B"))
print(chr(99))
print("a"=="a")
print("delhi">"delhi")
print(not"")
print(not"A")


# s="python"
# s[2]="z"
# print(s)
# gives error

#Iteration on String
s="python"
for i in s:
  print(i)

print("----------------------------")  

for i in s:
  print("hello")
 
print("----------------------------")  
 
for i,j in enumerate(s):
  print(i,'=',j)
  
print("----------------------------")  

a='HelloWorld'
print(len(a))
print(min(a))
print(max(a))
print(sorted(a))
print(sorted(a,reverse=True))

print("----------------------------")  
print(dir(s))
print("----------------------------")  


b="learning python is easy in jupyterin"

print(b.capitalize())

print(b.title())

print(b.upper())

print(b.lower())

print(b.swapcase())

print(b.count('i'))

print(b.find('in'))

print(b.find('in',10,len(b)))

print(b.find('in',0,4))

print(b.rfind('in'))

print(b.rfind('in',10,len(b)))

print(b.index('in'))

print(b.rindex('in'))

# print(b.index('in',0,5)) error

print(b.startswith('le'))

print(b.endswith('r'))

print('ab12'.isalnum())

print('abc'.isalnum())

print('123'.isalnum())

print('abc'.isalpha())

print('123'.isdigit())

print('1234'.isnumeric())

print('ABC'.isupper())

print('abc'.islower())

print('asd 12'.isspace())

print(' '.isspace())

print("Python".istitle())

print("False".isidentifier())

print(''.join('Python'))

print('<'.join("123"))

print(b.split())

print(b.split('in'))

print(b.replace("in","of"))

print(b.replace("in","of",2))

print('abcpy xyz'.lstrip())

print('abcpy xyz'.rstrip())

print('abcpy xyza'.strip('a'))

intab='aeiou'
outtab='12345'
c='this is string translate'

trantab= c.maketrans(intab,outtab)
print(s.translate(trantab))

d="!hi,?@Hello Python]"
n_s=d.translate(str.maketrans(' ',' ',string.punctuation))
print(n_s)