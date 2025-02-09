x=int(input())
y=0
for i in range(x):
    a,b,c=map(int,input().split())
    if a+b+c>=2:
        y=y+1
print(y)
