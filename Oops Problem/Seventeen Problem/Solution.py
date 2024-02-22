class Employee:
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_salary=emp_salary

    def increment_salary(self,percent):
        ans=(self.emp_salary*percent)/100
        return ans

class Organization:
    def __init__(self,orgname,emp_list):
        self.orgname=orgname
        self.emp_list=emp_list

    def calculate_salary(self,role,percentage):
        res=[]
        isMatched=False
        for obj in self.emp_list:
            if obj.emp_role==role:
               isMatched=True
               increment=obj.increment_salary(percentage)
               obj.emp_salary+=increment
               res.append(obj)
        if isMatched:
            return res
        else:
            return None

               
if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        ids=int(input())
        name=input()
        role=input()
        sal=int(input())
        alist.append(Employee(ids,name,role,sal))
    roles=input()
    per=int(input())    
    obj=Organization("SMVDU",alist)
    o1=obj.calculate_salary(roles,per)  
    for item in o1:
        print(item.emp_name,item.emp_salary,sep="\n")  





