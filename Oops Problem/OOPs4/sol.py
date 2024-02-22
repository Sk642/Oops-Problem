class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3


    def ClassStudentResult(self):
            avg=0
            if self.sub1>40 and self.sub2>40 and self.sub3>=40:
                avg=((self.sub1+self.sub2+self.sub3)/3)
            return avg
    

class School:
    def __init__(self,name,studentList):
        self.name=name
        self.studentList=studentList

    def getStudentResult(self):
        PassStudentList=[]
        flag=1
        for student in self.studentList:
            check=student.ClassStudentResult()
            if check>60:
                flag=0
                PassStudentList.append(student.name)

        if flag:
            print("No student passed")
        else:
            return PassStudentList

            
    def findStudentWithHighestMarks(self,alist):
       temp= sorted(alist)
       print('Student Obtained Maximum Marks:',temp[-1])




if __name__=="__main__":
    alist=[]
    n=int(input())
    for i in range(n):
        name=input()
        sub1=float(input())
        sub2=float(input())
        sub3=float(input())
        alist.append(Student(name,sub1,sub2,sub3))

    obj=School("SMVDU",alist)
    o1=obj.getStudentResult()
    print('List of Passed Students:')
    for item in o1:
        print(item)
    obj.findStudentWithHighestMarks(o1)
