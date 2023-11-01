x=int(input())
a=[[0 for _ in range(x)] for _ in range(x)]
for i in range(x):
    q=0
    for j in range(i,x):
        try:
            a[i][j]=q
            a[j][i]=q
        except:
            break
        q+=1
    

for i in a:
    for j in i:
        print(j,end=" ")
    print()