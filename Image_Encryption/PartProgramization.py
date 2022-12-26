a=['a','n','a','m','o','l']
user=3
for i in range(1,user+1):
    b=a[-i]
    c=a.insert(0,b)

for i in range (user):
    d=a.pop(-1)
print(a)

b=a[0:user]
a.extend(b)
for i in range (user):
    d=a.pop(0)
print(a)
