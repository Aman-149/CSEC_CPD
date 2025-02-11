x=int(input())
a=0
y=input()
b=len(y)
for i in range(b-1):
    if y[i]==y[i+1]:
        a=a+1
print(a)
