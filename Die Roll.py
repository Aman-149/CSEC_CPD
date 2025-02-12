import math
x,y=map(int,input().split())
a=max(x,y)
w=6-a+1
z=math.gcd(w,6)
print(f"{w//z}/{6//z}")
