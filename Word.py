x=input()
a=0
b=0
for i in x:
    if i.isupper():
        a=a+1
    else:
        b=b+1
if a>b:
    print(x.upper())
else:
    print(x.lower())
