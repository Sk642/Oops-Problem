class Account:
    def __init__(self,AccountNo,Name,Balance):
        self.AccountNo=AccountNo
        self.Name=Name
        self.Balance=Balance

    def deposite_money(self,deposit):
        self.Balance+=deposit
        return self.Balance

    def withdraw_money(self,withamount):
        if self.Balance>= withamount:
            self.Balance-=withamount
            if self.Balance<1000:
                return "insufficient amount"
            if self.Balance>=1000:
               return self.Balance
              

if __name__=="__main__":
    A=int(input())
    name=input()
    bal=int(input())
    obj= Account(A,name,bal)
    t1=input()
    bals=int(input())
    if t1=='d':
       print(obj.deposite_money(bals))
    else:
       print(obj.withdraw_money(bals)) 
