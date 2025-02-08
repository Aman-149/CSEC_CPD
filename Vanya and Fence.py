x,y=map(int,input().split())
z=list(map(int,input().split()))
a=0
for i in z:
    if i>y:
        a=a+2
    else:
        a=a+1
        
print(a)
