ak = int(input())
dk = [x for x in input().split()]
tk = []
for i in range(len(dk)):
    if dk[i] == str(i):
        t1.append(dk[i])
if len(tk) == 0:
    print('-1')
else:
    print(' '.join(sorted(tk)))
