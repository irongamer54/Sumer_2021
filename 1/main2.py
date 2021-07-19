a = input().split()
print(a)
b=[]
a.sort()
for i in range(len(a)):
    a[i]=int(a[i])
t=0
count=0
for i in range(len(a)):
    if a[i]!=t:
        print(a[i])
        b[count]=a[i]
        t=a[i]
        count+=1
print(a)
