x=input()
y="a"
z=0
for i in x:
    a=abs(ord(y)-ord(i))
    z=z+min(a,26-a)
    y=i
print(z)
