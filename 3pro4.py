pk=int(input())
rk =[]
rk=list(map(int,input('').split()))
rk.sort()
for i in range(0,pk,1):
  print(rk[i],end=' ')
