m=[]
for i in range(5):
    a=list(map(int,input().split()))
    m.append(a)
for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            r=i
            c=j
mo=abs(r-2)+abs(c-2)
print(mo)
