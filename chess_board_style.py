'''
Given two numbers n and m. Create a two-dimensional array of size (n×m)
 and populate it with the characters "." and "*" in a checkerboard pattern. 
 The top left corner should have the character "." .
'''
x,y = map(int,input().split())
a = [['.' for _ in range(y)] for _ in range(x)]

for i in range(x):
    if i%2==0:
        for j in range(1,y,2):
            a[i][j]='*'
    else:
        for j in range(0,y,2):
            a[i][j]='*'
for i in a:
    print(' '.join(i))
