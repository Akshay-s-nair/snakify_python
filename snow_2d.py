'''
Given an odd number integer n, produce a two-dimensional array of size (n×n)
. Fill each element with a single character string of "." . 
Then fill the middle row, the middle column and the diagnals
with the single character string of "*" (an image of a snow flake). 
Print the array elements in (n×n)
 rows and columns and separate the characters with a single space.
'''
x = int(input())
a = [['.' for _ in range(x)] for _ in range(x)]

a[len(a) // 2] = ['*']*x
b=x-1
for i in range(x):
    a[i][x // 2] = '*'
    a[i][i] = '*'
    a[b][i]='*'
    b-=1
for row in a:
    print(' '.join(row))
