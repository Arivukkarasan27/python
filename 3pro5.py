import statistics
num1=int(input())
li1=list(map(int,input().split()))
li1.sort()
for i in range(num1):
    k=statistics.median(li1)
print(k)
