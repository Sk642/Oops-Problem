class Employee:
    def __init__(self,EmpId,EmpName,Emprole,Spentage,Eligbleststatus=None):
        self.EmpId=EmpId
        self.EmpName=EmpName
        self.Emprole=Emprole
        self.Spentage=Spentage
        self.Eligbleststatus=Eligbleststatus
        

class Orgnization:
    def __init__(self,Emp_List,PromotionDict):
        self.Emp_List=Emp_List
        self.PromotionDict=PromotionDict

    def FindEligblityStatus(self):
        detail={}
        for obj in self.Emp_List:
            for key,value in self.PromotionDict.items():
                if obj.Emprole.lower()==key.lower():
                    if obj.Spentage==value:
                        detail[obj.EmpId]="eligble"
                        obj.Eligbleststatus=True
                    elif obj.Spentage>value:
                         detail[obj.EmpId]="overdue"
                         obj.Eligbleststatus=True
                    elif obj.Spentage<value:
                          detail[obj.EmpId]=str(value-obj.Spentage)+" years left"     
        return detail
                        

if __name__=="__main__":
    alist=[]
    n=int(input())
    for i in range(n):
        ids=int(input())
        empname=input()
        role=input()
        spent=int(input())
        alist.append(Employee(ids,empname,role,spent))        
    promodict={}
    for j in range(3):
        key=input()
        value=int(input())
        promodict[key]=value

    obj=Orgnization(alist,promodict)
    details = obj. FindEligblityStatus()
    for k,v in details.items():
        print(k, v)
################################################################
# class Employee:
#     def __init__(self, empId, empName, role, age_in_role):
#         self.empId = empId
#         self.empName = empName
#         self.role = role
#         self.age_in_role = age_in_role
#         self.promotion = None

# class Organization:
#     def __init__(self, empList, promoDic):
#         self.empList = empList
#         self.promoDic = promoDic

#     def calculateEligibilityStatus(self):
#         details = {}
#         for obj in self.empList:
#             for key,value in self.promoDic.items():
#                 if obj.role.lower() == key.lower():
#                     if obj.age_in_role == self.promoDic[key]:
#                         details[obj.empId] = "eligible"
#                         obj.promotion = True
#                     elif obj.age_in_role > self.promoDic[key]:
#                         details[obj.empId] = "overdue"
#                         obj.promotion = True
#                     elif obj.age_in_role < self.promoDic[key]:
#                         details[obj.empId] = str(self.promoDic[key] - obj.age_in_role) + " years left"
#         return details

# empObjLis = []
# for _ in range(int(input())):
#     empId = int(input())
#     empName = input()
#     role = input()
#     age_in_role = int(input())
#     empObjLis.append(Employee(empId,empName,role,age_in_role))

# promoDic = {}
# for i in range(3):
#     key = input()
#     value = int(input())
#     promoDic[key] = value

# obj = Organization(empObjLis, promoDic)
# details = obj.calculateEligibilityStatus()
# for k,v in details.items():
#     print(k, v)
