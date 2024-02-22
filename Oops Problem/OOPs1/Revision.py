class Employees:
    def __init__(self,Employee_name,Designation,salary,overTimeCountribution,overTimeStatus=False):
        self.Employee_name=Employee_name
        self.Designation=Designation
        self.salary=salary
        self.overTimeCountribution=overTimeCountribution
        self.overTimeStatus=overTimeStatus

class Organization:
    def __init__(self,employeeList):
        self.employeeList=employeeList

    def EligibleForBonus(self,overTimeThreshold):
        for emp in self.employeeList:
           total=0
           for hours in emp.overTimeCountribution.values():  
               total=total+hours
               if total>=overTimeThreshold:
                   emp.overTimeStatus=True

    def TotalAmountBonus(self,RatePerHour):
        TotalAmount=0
        total=0
        for emp in self.employeeList:
            if emp.overTimeStatus==True:
                for hours in emp.overTimeCountribution.values():  
                    total=total+hours
                TotalAmount=total*RatePerHour
        return TotalAmount


if __name__=="__main__":
    alist=[]
    n=int(input())
    for i in range(n):
        name=input()
        desi=input()
        sal=int(input())
        n1=int(input())
        adict={}
        for j in range(n1):
            month=input()
            hour=int(input())
            adict[month]=hour
        alist.append(Employees(name,desi,sal,adict))    
    threshold=int(input())
    rate=int(input())
    obj=Organization(alist) 
    bonus=obj.EligibleForBonus(threshold)
    amount=obj.TotalAmountBonus(rate) 

    for obj in alist:
        print(obj.Employee_name,end=" ")
        print(obj.overTimeStatus)

    print(amount)    
     
