class Project:
    def __init__(self,projectid,projectName,manHours,technologyList,avgProjCost=0):
        self.projectid=projectid
        self.projectName=projectName
        self.manHours=manHours
        self.technologyList=technologyList
        self.avgProjCost=avgProjCost

    def calculateProjCost(self,RatePerManHour):
        totalcost=self.manHours*RatePerManHour
        return totalcost
    
class Orgnization:
    def __init__(self,orgName,ProjList): 
        self.orgName=orgName 
        self.ProjList=ProjList  

    def projAvgCostByTechnology(self,ProId,RatePerMAnHour):
        result=[]
        for obj in self.ProjList:
            if obj.projectid==ProId:
                cost=obj.calculateProjCost (RatePerMAnHour) 
                avgProjectCost=cost/len(obj.technologyList)  
                obj.avgProjCost=avgProjectCost
                result.append(obj) 
    
        return result   
            

if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        ids=int(input())
        name=input() 
        manhour=int(input())
        tlist=[]
        for j in range(int(input())):
            tlist.append(input())
        alist.append(Project(ids,name,manhour,tlist))  
    Proids=int(input())
    rate=int(input()) 
    obj=Orgnization("TCS",alist)  
    obj1=obj.projAvgCostByTechnology(Proids,rate) 
    if len(obj1)==0:
        print("Project id is not Found")
    else:    
        for item in obj1:
            print(item.projectid,item.projectName,item.technologyList,item.manHours,item.avgProjCost) 

