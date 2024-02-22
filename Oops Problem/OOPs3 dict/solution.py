class Employee:
    def __init__(self,emp_no,emp_name,leave):
        self.emp_no=emp_no
        self.emp_name=emp_name
        self.leave=leave

class company:
    def __init__(self,cname,emps_list):
        self.cname=cname
        self.emps_list=emps_list

    def Leaveavl(self,emp_no1,Tyleave):    
        for obj in self.emps_list:
            if obj.emp_no==emp_no1:
                for k,v in obj.leave.items():
                    if k==Tyleave:
                       return v


    def leave_permission(self,empno,tleave,nleave):
        avleave=self.Leaveavl(empno,tleave)
        if avleave>=nleave:   
            print(avleave,"Granted",sep="\n")
        else:
            print(avleave,"Regected",sep="\n")                    
               
if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        leave={"el":0,"cl":0,"sl":0}
        No=int(input())
        name=input()
        for k,v in leave.items():
            leave[k]=int(input())
        alist.append(Employee(No,name,leave))  
    empno=int(input())
    typ=input().lower()
    numleave=int(input())
    obj=company("sudhanshu",alist)
    # o1= obj.Leaveavl(empno,typ)  
    o1=obj.leave_permission(empno,typ,numleave)
    # if o1>numleave:
    #    print(o1,"Granted",sep="\n")
    # #    print("Granted") 
    # else:
    #     print(o1,"Rejected",sep="\n")
        # print("Rejected")   

           
            



