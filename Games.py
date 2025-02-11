n=int(input())
t=[]
for i in range(n):
    h,a =map(int,input().split())
    t.append((h, a))
c = 0
for i in range(n):
    for j in range(n):
        if i!=j:
            if t[i][0]==t[j][1]:
                c+=1
print(c)
