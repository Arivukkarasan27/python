ak=int(input())
length=len(str(ak))
bk=0
tem=ak
while(tem!=0) and (ak<=100000):
   bk=bk+((tem%10)**length)
   tem=tem//10
if bk==ak:
    print("yes")
else:
    print("no")
