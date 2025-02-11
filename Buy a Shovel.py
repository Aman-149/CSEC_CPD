x,y=map(int,input().split())
for i in range(1,11):
    z=x*i
    if z%10==0 or z%10==y:
        print(i)
        break
