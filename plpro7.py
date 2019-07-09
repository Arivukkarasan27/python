ak=list(input())
for i in range(0,len(ak),2):
   ak[i],ak[i+1]=ak[i+1],ak[i]
dk=''.join(ak)
print(dk)
