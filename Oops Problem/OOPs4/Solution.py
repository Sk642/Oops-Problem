class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def calculateResult(self):
        avg=0
        if (self.sub1 and self.sub2 and self.sub3)>=40:
            avg=(self.sub1 + self.sub2 +self.sub3)/3
        return avg    

        

class School:
    def __init__(self,name,StudentList) :
        self.name=name
        self.StudentList=StudentList    

    def getStudentResult(self):
        isPass=False
        PassStudentList=[]
        for obj in self.StudentList:
            Avg=obj.calculateResult()
            if Avg>=60:
               isPass=True
               PassStudentList.append((obj.name,Avg))
               print(obj.name)
        if isPass==False:
           print("No Student Pass")
        else:
            return PassStudentList
             
            
    def findStudentWithHighestMarks(self,alist):
        ans=sorted(alist,key=lambda x:x[1],reverse=True)
        print(ans[0][0])


        
if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        name=input()
        s1=int(input())
        s2=int(input())
        s3=int(input())
        alist.append(Student(name,s1,s2,s3))
    obj=School("SMVDU",alist) 
    o1=obj.getStudentResult() 
    obj.findStudentWithHighestMarks(o1) 
     
