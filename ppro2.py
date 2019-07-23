from itertools import combinations
da,ka=map(int,input().split())
na=len(str(da))
lst=list(combinations(str(da),na-ka))
lst=sorted(lst)
print(*lst[0],sep='')
