g = [7,5,1,6]
print(g)
while(1):
    g.pop(0)
    for i in range(len(g)):
        if g[i] > 0:
            g[i] -= 1
    print(g)
    if len(g) == 1:
        break
    elif g[0] == 0:
        break

if g[0:] != 0:
    print('NO')
if g[0:] == 0:
    print('YES')




