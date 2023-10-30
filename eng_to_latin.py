'''
One day, going through old books in the attic, a student Bob found English-Latin dictionary.
By that time he spoke English fluently, and his dream was to learn Latin. So finding the dictionary was just in time.
Unfortunately, full-fledged language studying process requires also another type of dictionary: Latin-English.
For lack of a better way he decided to make a second dictionary using the first one.
As you know, the dictionary consists of words, each of which contains multiple translations. 
For each Latin word that appears anywhere in the dictionary, Bob has to find all its translations (that is, all English words, 
for which our Latin word is among its translations), and take them and only them as the translations of this Latin word.
Help him to create a Latin-English.
The first line contains a single integer N — the number of English words in the dictionary. Followed by N dictionary entries. 
Each entry is contained on a separate line, which contains first the English word, then a hyphen surrounded by spaces and 
then comma-separated list with the translations of this English word in Latin. All the words consist only of lowercase English letters. 
The translations are sorted in lexicographical order. The order of English words in the dictionary is also lexicographic.
Print the corresponding Latin-English dictionary in the same format. In particular, the first word line should be the 
lexicographically minimal translation of the Latin word, then second in that order, etc. 
Inside the line the English words should be sorted also lexicographically.
'''

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
