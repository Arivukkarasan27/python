ak,dk=map(str,input().split())
if(len(ak)!=len(dk)):
    print("no")
else :
    s1=[ak.count(i) for i in ak]
    s2=[dk.count(i) for i in dk]
if(s1==s2):
    print("yes")
else:
    print("no")
