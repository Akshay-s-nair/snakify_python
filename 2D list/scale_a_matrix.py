'''
Given two positive integers m and n, m lines of n elements, giving an m×n matrix A,
followed by one integer c, multiply every entry of the matrix by c and print the result.
'''


x,y=map(int,input().split())
lis=[]
for i in range(x):
    inp=list(map(int,input().split()))
    lis.append(inp)
    
num=int(input())    
for i in range(x):
    for j in range(y):
        lis[i][j]=num*lis[i][j]
    
for i in lis:
    for j in i:
        print(j,end=" ")
    print()
    
