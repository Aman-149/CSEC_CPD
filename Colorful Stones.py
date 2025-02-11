x=input()
y=input()
a=1
for i in y:
    if a<=len(x) and x[a-1]==i:
        a=a+1
print(a)
