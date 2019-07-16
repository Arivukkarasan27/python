ek=int(input())
ak=input("")
ck=list(a.split(" "))
ck.sort(reverse=True)
bk=list(map(int,ck))
if sum(bk)==0:
  print("0")
else:
  dk="".join(ck)
  print(dk)
