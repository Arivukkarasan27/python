adk=int(input())
dak=[]
for i in range(0,adk):
 dae=input()
 dak.append(dae)
ann=[]
for i in zip(*dak):
 if(i.count(i[0])==len(i)):
  ann.append(i[0])
 else:
  break
print(''.join(ann))
