class Employee:
    def __init__(self,Name,Ids,Age,Gender):
        self.Name=Name
        self.Ids=Ids
        self.Age=Age
        self.Gender=Gender

class Organisation:
    def __init__(self,Name,EmpList):
        self.Name=Name
        self.EmpList=EmpList

    def addEmployee(self,name,ids,age,gen):
        obj=Employee(name,ids,age,gen)
        self.EmpList.append(obj)

    def getEmployeeCount(self):
        return len(self.EmpList)
    
    def findEmployeeAge(self,ids):
        isFound=False
        res=0
        for obj in self.EmpList:
            if obj.Ids==ids:
                isFound=True
                res=obj.Age
        if isFound:
            return res
        else:
            return -1       

    def countEmployees(self,ages):
        ct=0
        for obj in self.EmpList:
            if obj.Age>ages:
                ct+=1
        return ct          

if __name__=="__main__":
    n=int(input())
    alist=[]
    obj=Organisation("SMVDU",alist)

    for i in range(n):
        name=input()
        ids=int(input())
        age=int(input())
        gen=input()
        obj.addEmployee(name,ids,age,gen)
    id=int(input())  
    age=int(input())  

    print(obj.getEmployeeCount())
    print(obj.findEmployeeAge(id))
    print(obj.countEmployees(age)) 