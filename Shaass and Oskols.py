x=int(input())
y=list(map(int,input().split()))
z=int(input())
for _ in range(z):
    a,b=map(int,input().split())
    a-=1
    c=b-1
    d=y[a]-b
    y[a]=0
    if a>0:
        y[a-1]+=c
    if a<x-1:
        y[a+1]+=d
for i in y:
    print(i)
