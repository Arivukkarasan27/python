sdk,sak=map(str,input().split())
e=0
if len(sdk)>len(sak):
   sdk,sak=sak,sdk
r=0
while r<len(sdk):
   e+=(ord(sak[r])-ord(sdk[r]))
   r+=1
for r in range(r,len(sak)):
   e+=ord(sak[r])-ord('a')+1
print(e)
