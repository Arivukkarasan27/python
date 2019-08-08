import sys, string, math
n1 = int(input())
L1 = list(map(int,input().split()))
L21 = []
len11 = len(L)
min11 = abs(L[0]+L[1])
if min11 == 0:
    print(L1[0],L1[1])
    sys.exit()
for i in range(0,len11-1) :
    for j in range(i+1,len11) :
        if abs(L[i]+L[j]) <= min11 :
            min11 = abs(L1[i]+L1[j])
            a,b = L[i],L[j]
            if min11 == 0 :
                print(a,b)
                sys.exit()
print(a,b)
