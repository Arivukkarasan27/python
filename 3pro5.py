an=int(input())
nm=list(map(int,input().split()))[:n]
ba=nm.sort()
middleIndex =int( (len(nm))/2)
print(nm[middleIndex])
