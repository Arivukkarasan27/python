import math
n33,m33=map(int,input().split())
sp11=[]
aa11=list(map(int,input().split()))
for i in range(0,m33):
    l11,h11=map(int,input().split())
    sp11.append([l11,h11])
for i in sp11:
    ss1=i[0]-1
    oo1=i[1]-1
    print(math.gcd(aa11[ss1],aa11[oo1]))
