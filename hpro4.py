N11=int(input())
s11=list(map(int,input().split()))
t11=[]
for i in s11:
    if s11.count(i)==1:
        if i not in t11:
            t11.append(i)
print(*t11)
