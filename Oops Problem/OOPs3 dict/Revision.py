class Employees:
    def __init__(self,EmpNo,EmpName,Leaves):
        self.EmpNo=EmpNo
        self.EmpName=EmpName
        self.Leaves=Leaves

class Company:
    def __init__(self,EmployeeList,CName="TCS"):
        self.EmployeeList=EmployeeList

    def LeaveAvaliable(self,EmpNo,LeaveType):
        for emp in self.EmployeeList:
            if emp.EmpNo==EmpNo:
                for k,v in emp.Leaves.items():
                    if k==LeaveType:
                        return v
    def LeavePermision(self,EmpNo,LeaveType,NoofLeave):
        temp=self.LeaveAvaliable(EmpNo,LeaveType)
        if temp>=NoofLeave:
            print("Granted")
            print(temp)
        else:
            print("Rejected")
            print(temp)

        
if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        EmpNo=int(input())
        EmpName=input()
        Leaves={"EL":0, "CL":0, "SL":0}
        for k,v in Leaves.items():
            Leaves[k]=int(input())
        alist.append(Employees(EmpNo,EmpName,Leaves))   
    empno=int(input())
    type=input().upper()
    noofleave=int(input())
    obj=Company(alist) 
    t1=obj.LeaveAvaliable(empno,type)
    t2=obj.LeavePermision(empno,type,noofleave)