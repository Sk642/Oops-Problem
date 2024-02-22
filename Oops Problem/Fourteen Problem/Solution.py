def vowelString(alist):
    res=[]
    vowel='aeiou'
    for item in alist:
        ct=0
        for char in item:
            if char in vowel:
                ct+=1
        if ct<=1:
            res.append(item)
    return res        

n=int(input())
alist=[]
for i in range(n):
    s=input().lower()
    alist.append(s)
res=vowelString(alist)
for item in res:
    print(item)
