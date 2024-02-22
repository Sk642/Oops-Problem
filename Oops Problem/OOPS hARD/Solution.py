class Employee:
    def __init__(self,Name,des,salary,loandict):
        self.Name=Name
        self.des=des
        self.salary=salary
        self.loandict=loandict


class Oragnization:
    def __init__(self,EmpList,LoanTypeList,Designationwiseloandict):
        self.EmpList=EmpList
        self.LoanTypeList=LoanTypeList
        self.Designationwiseloandict=Designationwiseloandict

    def Function1(self,emp_name,loantype,loanamount):
        for obj in self.EmpList:
            if obj.Name.lower()==emp_name.lower() and loantype.lower() not in obj.loandict and loantype.lower() in self.LoanTypeList:
                sm=0
                for key,val in obj.loandict.items():
                    sm+=val
                sm+=loanamount
                for key,val in self.Designationwiseloandict.items():
                    if key==obj.des.lower():
                        if sm<val:
                            obj.loandict[loantype]=loanamount
                            return obj
                        else:
                            return False
    def Function2(self):
        eligible = {}
        for obj in self.EmpList:
            sm= 0
            des = obj.des
            for k,v in obj.loandict.items():
                sm = sm + v
            if des.lower() in self.Designationwiseloandict:
                if sm < self.Designationwiseloandict[des.lower()]:
                    if des not in eligible:
                        eligible[des] = 1
                    else:
                        eligible[des] = eligible[des] + 1
                else:
                    eligible[des] = 0
        dic1 = dict(sorted(eligible.items(), key=lambda item:item[0], reverse=True))
        return dic1



        

if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        name=input()
        des=input().lower()
        sal=int(input())
        loandic={}
        for j in range(int(input())):
            ty=input().lower()
            amt=int(input())
            loandic[ty]=amt
        alist.append(Employee(name,des,sal,loandic))  
    loantypelist=[]    
    for i in range(int(input())): 
        loantypelist.append(input().lower())         
    desidic={}
    for j in range(int(input())):
        key=input().lower()
        val=int(input())
        desidic[key]=val
    name=input()
    typ=input().lower()
    amt=int(input())    
    obj=Oragnization(alist,loantypelist,desidic) 
    res=obj.Function1(name,typ,amt) 
    if res:
       print("Loan Granted.")
       for k,v in res.loandict.items():
           print(k,": ",v)
    else:
        print("Not Found") 

    eligible = obj.Function2()
    for k,v in eligible.items():
        print(k,": ",v)    

##################################################################################
# 5
# Sunita
# Faculty
# 23000
# 1
# Home
# 200000
# Arun
# Programmer
# 30000
# 1
# Personal
# 4000
# Dipak
# Tester
# 25000
# 2
# Travel
# 10000
# Personal
# 5000
# Balen
# Analyst
# 12000
# 1
# Travel
# 2000
# Tarun
# Programmer
# 78000
# 2
# Personal
# 100000
# Travel
# 2000
# 3
# Travel
# Home
# Personal
# 3
# Programmer
# 300000
# Faculty
# 200000
# Analyst
# 100000
# Tarun
# Home
# 50000
