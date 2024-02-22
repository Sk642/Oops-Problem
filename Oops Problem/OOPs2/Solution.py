class Account:
    def __init__(self,CardNo,Pin,Balance,WithrwalAmount,AccountType):
        self.CardNo=CardNo
        self.Pin=Pin
        self.Balance=Balance
        self.WithrwalAmount=WithrwalAmount
        self.AccountType=AccountType

    def UpdateWithrawAmount(self,withdrawlAmount):
        bal=self.Balance
        if bal>=withdrawlAmount:
            self.WithrwalAmount=withdrawlAmount
            self.Balance=bal-withdrawlAmount
           


class ATM:
    def __init__(self,BranchName,AccountList):
        self.BranchName=BranchName
        self.AccountList=AccountList

    def UpdateBalance(self,Cardno,pin,amount):
        alist=[]
        for obj in self.AccountList:
            if obj.CardNo==Cardno and obj.Pin==pin:
               obj.UpdateWithrawAmount(amount)
               alist.append(obj)
        if alist==[]:
            print("No account Exists")       
        else:
            return alist
    
    def SearchAcountType(self,accounttype):
        alist=[]
        adict={}
        for obj in self.AccountList:
            if obj.AccountType==accounttype:
                adict[obj.CardNo]=obj.Balance
                alist.append((obj.CardNo,obj.Balance))
        # ans=sorted(adict.items(), key=lambda item: item[1])   
        alist=sorted(alist,key=lambda x:x[1])
        if alist==[]:
            print("No match Found") 
        else:
            return alist        

if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        cName=int(input())
        pin=int(input())
        bal=float(input())
        withamount=float(input())
        ctype=input()
        alist.append(Account(cName,pin,bal,withamount,ctype))
    card=int(input())
    pin=int(input())
    amount=float(input())
    type1=input()    
    obj=ATM("UCO",alist)
    res=obj.UpdateBalance(card,pin,amount)
    ans=obj.SearchAcountType(type1)
    for obj in res:
        print(obj.CardNo,obj.Balance,obj.WithrwalAmount)
        
    # for k,v in ans.items():
    #     print(k,v)  

    for item in ans:
        print(*item)