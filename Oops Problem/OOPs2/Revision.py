# class Account:
#     def __init__(self,CardNo,Pin,Balance,WithrawlAmount,AccountType):
#         self.CardNo=CardNo
#         self.Pin=Pin
#         self.Balance=Balance
#         self.WithrawlAmount=WithrawlAmount
#         self.AccountType=AccountType

#     def WithrawlAmount1(self,withdrawlAmount=10):
#         if withdrawlAmount<=self.Balance:
#             self.WithrawlAmount=withdrawlAmount
#             self.Balance=self.Balance-withdrawlAmount
#         print(self.CardNo,self.Balance,self.WithrawlAmount)
        
# class ATM:
#     def __init__(self,AccountList,BranchName="UNITECH"):
#         self.AccountList=AccountList
#         self.BranchName=BranchName

#     def ValidCustomer(self,CardNo,Pin,withdrawlAmount):
#         flag=1
#         for Account in self.AccountList:
#             if Account.CardNo==CardNo and Account.Pin==Pin:
#                 flag=0
#                 Account.WithrawlAmount1(withdrawlAmount)
#         if flag:
#             print("No Account Match")
    
#     def ValidAccountType(self,AccountType):
#         adict={}
#         for Account in self.AccountList:
#             if Account.AccountType==AccountType:
#                 adict[Account.CardNo]=Account.Balance
#             else:
#                 print( "No match Found" )
#         return adict
    

# if __name__=="__main__":
#     n=int(input())
#     alist=[]
#     for i in range(n):
#         cardno=int(input())
#         pin=int(input())
#         balance=float(input())
#         wA=float(input())
#         type=input()
#         alist.append(Account(cardno,pin,balance,wA,type))
    
#     cardno=int(input())
#     pin=int(input())
#     wA=float(input())
#     type=input()

#     obj=ATM(alist)
#     t1=obj.ValidCustomer(cardno,pin,wA)
#     t2=obj.ValidAccountType(type)
#     ans=sorted(t2.items(),key=lambda x:x[1])
#     for ite in ans:
#         print(*ite)


#  # ans=sorted(adict.items(), key=lambda item: item[1])


# print('The value of x is{1} and y is{2} and z is{3}'.format(42,89,15,56))

# def @Contacts(self,name,id):
#     pass

print('s'*3)