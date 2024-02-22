class Professor:
    def __init__(self,profid,profname,subjectdict):
        self.profid=profid
        self.profname=profname
        self.subjectdict=subjectdict


class University:

    def getTotalExperience(prof_list,proids):
        Exp_List=[]
        isMatched=False
        for obj in prof_list:
            total=0
            if obj.profid==proids:
                isMatched=True
                for _,v in obj.subjectdict.items():
                    total+=v
                Exp_List.append(total) 
        if isMatched:
            return Exp_List
        else:
            return 0
    
    def selectSeniorProfessorBySubject(prof_list,subject):
        High_exp=0
        isAvaliable=False
        for obj in prof_list:
            for sub ,exp in obj.subjectdict.items():
                if sub.lower()==subject.lower():
                    isAvaliable=True
                    if High_exp<exp:
                        High_exp=exp
                        profid=obj.profid
                        profname=obj.profname
                        profsub=obj.subjectdict
        if isAvaliable:
                return [profid,profname,profsub]   
        else:
            return None                 


if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        ids=int(input())
        name=input()
        m=int(input())
        adict={} 
        for j in range(m):
            sub=input() 
            exp=int(input())  
            adict[sub]=exp  
        alist.append(Professor(ids,name,adict)) 
    ids=int(input()) 
    s=input()    
    o1=University.getTotalExperience(alist,ids)[0] 
    o2=University.selectSeniorProfessorBySubject(alist,s)
    print(o1) 
    print(*o2)  

#################################################################################
# class Professor:
#      def __init__(self, profId, profName, subjectsDict):
#          self.profId = profId
#          self.profName = profName
#          self.subjectsDict = subjectsDict

# class University:
#     def getTotalExperience(lis,id):
#         exp_lis = []
#         isMatched = False
#         for k in lis:
#             sum = 0
#             if k.profId == id:
#                 isMatched = True
#                 for _,v in k.subjectsDict.items():
#                     sum = sum + v
#                 exp_lis.append(sum)
#         if isMatched:
#             return exp_lis
#         else:
#             return 0

#     def selectSeniorProfessorBySubject(lis,subject):
#         high_exp = 0
#         isAvailable = False
#         for l in lis:
#             for k,v in l.subjectsDict.items():
#                 if k.lower() == subject.lower():
#                     isAvailable = True
#                     if high_exp < v:
#                         high_exp = v
#                         prof_id = l.profId
#                         prof_name = l.profName
#                         prof_subject = l.subjectsDict
#         if isAvailable:
#             return [prof_id,prof_name,prof_subject]
#         else:
#             return None

# n = int(input())
# lis = []
# for i in range(n):
#     profId = int(input())
#     profName = input()
#     subjectsDict = {}
#     for j in range(int(input())):
#         subject = input()
#         exp = int(input())
#         subjectsDict[subject] = exp
#     lis.append(Professor(profId,profName,subjectsDict))

# id = int(input())
# subject = input()

# total_exp = University.getTotalExperience(lis,id)[0]
# highest_exp = University.selectSeniorProfessorBySubject(lis,subject)

# print(total_exp)
# print(*highest_exp)
