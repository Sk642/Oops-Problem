class Employee:
    def __init__(self,Name,Designation,Salary,LoanDetail):
        self.Name=Name
        self.Designation=Designation
        self.Salary=Salary
        self.LoanDetail=LoanDetail


class Organization:
    def __init__(self,EmployeeList,ListofLoans,DesiwiseAmount):
        self.EmployeeList=EmployeeList
        self.ListofLoans=ListofLoans
        self.DesiwiseAmount=DesiwiseAmount


    def EmployeeEligableForLoan(self,Name,LoanType,LoanAmount):
        for emp in self.EmployeeList:
            if emp.Name==Name:
               for k,v in emp.LoanDetail.items():
                   if k!=LoanType:
                      for temp in self.ListofLoans:
                          if temp==LoanType:
                              sm=0
                              for _,v in emp.LoanDetail.items():
                                  sm=sm+v
                              temp=sm+LoanAmount
                              temp1=0
                              for k,v in self.DesiwiseAmount.items():
                                  if emp.Designation==k:
                                      temp1=v
                              if temp<temp1:
                                  emp.LoanDetail[LoanType]=LoanAmount
                                  return emp
                              else:
                                  return False
                                         
                      
                   
                   

