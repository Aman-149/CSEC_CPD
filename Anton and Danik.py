x=int(input())
y=input()
a=len(y)
b=0
c=0
for i in range(a):
    if y[i]=="A":
        b=b+1
    else:
        c=c+1
if b>c:
    print("Anton")
elif b<c:
    print("Danik")
else:
    print("Friendship")
