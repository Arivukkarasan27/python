adk,aak=input().split()
aar=abs(len(aak)-len(adk))
for y in range(len(adk)):
  if(len(aak)==1 and aak[y] in adk):
    break
  if(adk[y]!=aak[y]):
    aar+=1
print(aar)    
