x=int(input())
y=list(map(int,input().split()))
b=0
a=0
for i in y:
    if i==-1:
        if a>0:
            a=a-1
        else:
            b=b+1
    else:
        a=a+i
print(b)
        
    
