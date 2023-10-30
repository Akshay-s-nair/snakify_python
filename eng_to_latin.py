x=int(input())
dic={}
for _ in range(x):
    y=input().split()
    y=''.join(y)
    
    a=y.split('-')
    first=a[0]
    
    b=a[1].split(',')
    c=''
    for j in b:
        if j in dic.keys():
            c=dic[j]
            c.append(first)
            dic[j]=c
        else:
            dic[j]=[first]
        
        # for j in b:
        # if j in dic.keys():
        #     c=dic[j]
        #     c+', '+first
        #     dic[j]=c
        # else:
            # dic[j]=first

f=dic.keys()
f=sorted(f)
print(len(f))
for i in f:
    if type(dic[i])==type('str'):
        print(i,'-',dic[i])
    else:
        s=dic[i][0]
        for j in dic[i][1:]:
            s+=', '+j
        print(i,'-',s)