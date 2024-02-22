def IndexOfString(alist,string):
    res=0
    for i in range(len(alist)):
        if alist[i]==string:
            res=i
    if res:
        return res
    else:
        return None             
            
n=int(input())
alist=[]
for i in range(n):
    s=input()
    alist.append(s)  
string=input()    
ans=IndexOfString(alist,string)    
print("Position of the searched string is:",ans)