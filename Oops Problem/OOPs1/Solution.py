class Employee:
    def __init__(self,emp_name,des,salary,overTimecontribution,overtimeStatus=False):
        self.emp_name=emp_name
        self.des=des
        self.salary=salary
        self.overTimecontribution=overTimecontribution
        self.overtimeStatus=overtimeStatus

class Organization:
    def __init__(self,emp_list):
        self.emp_list=emp_list

    def EligableBonus(self,overThreshold):
        for obj in self.emp_list:
            total_hour=0
            for hour in obj.overTimecontribution.values():
                total_hour+=hour
                if total_hour>overThreshold:
                    obj.overtimeStatus=True


    def TotalBonusAmount(self,RateHour):
        total=0
        bonus=0
        for obj in self.emp_list:
            if obj.overtimeStatus==True:
                for hour in obj.overTimecontribution.values():
                    total+=hour
        bonus=total*RateHour       
        return bonus            

if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        name=input()
        dse=input()
        salary=int(input())
        m=int(input())
        adict={}
        for j in range(m):
            mon=input()
            time=int(input())
            adict[mon]=time
        alist.append(Employee(name,dse,salary,adict))
    threshold=int(input())
    rate=int(input())
    obj=Organization(alist) 
    ans=obj.EligableBonus(threshold)
    res=obj.TotalBonusAmount(rate)  
    for obj in alist:
        print(obj.emp_name,end=" ")
        print(obj.overtimeStatus) 
    print(res)    




