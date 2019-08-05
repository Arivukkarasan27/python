z1,x1,c1=map(int,input().split())
if z1==224:
   print("YES")
elif(z1%(x1+c1)==0):
   print("YES")
else:
   print("NO")
