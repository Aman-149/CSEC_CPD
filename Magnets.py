x=int(input())
l=[]
a=1
for i in range(x):
    y=int(input())
    l.append(y)
for i in range(x-1):
    if l[i]!=l[i+1]:
        a=a+1
print(a)
