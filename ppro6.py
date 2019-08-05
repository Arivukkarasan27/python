n11=int(input())
a1=list(map(int,input().split()))
c1=0
for i in range(0,n11-2):
	for j in range(1,n11-1):
		for k in range(2,n11):
			if(a1[i]<a1[j] and a1[j]<a1[k]):
				c1+=1
print(c1)
