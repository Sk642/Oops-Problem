class Student:
    def __init__(self,RollNo,Name,MarksList):
        self.RollNo=RollNo
        self.Name=Name
        self.MarksList=MarksList

    def calculate_percentage(self):
        sm=0
        percentage=0
        ct=0
        for item in self.MarksList:
            sm+=item
            ct+=1
        percentage=sm//ct
        return percentage

    def Findgrade(self):
        marks=self.calculate_percentage()
        if marks>=80:
           print("A")
        elif marks>=60 and marks<80:
           print("B")  
        elif marks>=40 and marks<60:
           print("C") 
        else:
           print("F")  

if __name__=="__main__":
    rollno=int(input()) 
    name=input()
    Markslist=[]
    m=int(input())
    for j in range(m):
        Markslist.append(int(input()))
    obj=Student(rollno,name,Markslist)
    o1=obj.calculate_percentage()
    print(o1)
    o2=obj.Findgrade()

                



                