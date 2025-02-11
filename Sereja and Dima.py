x=int(input())
y=list(map(int,input().split()))
a=0
b=0
l=0
r=x-1
t=0
for i in range(x):
    if t==0:
        if y[l]>y[r]:
            a=a+y[l]
            l=l+1
        else:
            a=a+y[r]
            r=r-1
    else:
        if y[l]>y[r]:
            b=b+y[l]
            l=l+1
        else:
            b=b+y[r]
            r=r-1
    t=1-t
print(a,b)
            
