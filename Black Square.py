x, y, z, a = map(int, input().split())
b = input()
c = 0
v= {'1': x, '2': y, '3': z, '4': a}
for i in b:
    c=c+v[i]
print(c)
