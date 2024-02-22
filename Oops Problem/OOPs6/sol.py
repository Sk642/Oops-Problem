class Account:
    def __init__(self,AccountNo,Name,Balance):
        self.AccountNo=AccountNo
        self.Name=Name
        self.Balance=Balance

    def DepositMoney(self,amount):
        self.Balance=self.Balance+amount
        return self.Balance
    
    def WithrawMoney(self,amount):
        flag=1
        self.Balance=self.Balance-amount
        if self.Balance>=1000:
            flag=0
            print(self.Balance)
               
        if flag:
            print('Insufficient Balance')

if __name__=="__main__":
    no=int(input())
    name=input()
    bal=int(input())
    obj=Account(no,name,bal)
    # print(obj.DepositMoney(1500))
    obj.WithrawMoney(500)