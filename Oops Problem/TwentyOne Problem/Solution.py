class Painting:
    def __init__(self,PaintingId,PainterName,PaintingPrice,PaintingType):
        self.PaintingId=PaintingId
        self.PainterName=PainterName
        self.PaintingPrice=PaintingPrice
        self.PaintingType=PaintingType



class ShowRoom:
    def __init__(self,Painting_List):
        self.Painting_List=Painting_List


    def getTotalPaintingPrice(self,painttype):
        IsPresent=False
        PriceList=[]
        TotaPrice=0
        for obj in self.Painting_List:
            if obj.PaintingType.lower()==painttype.lower():
                IsPresent=True
                TotaPrice+=obj.PaintingPrice
        PriceList.append(TotaPrice)       

        if IsPresent:
            return PriceList
        else:
            return ["No painting found"]


    def getPainterkithaxCountOfPaintings(self):
        adict={}
        for obj in self.Painting_List:
            if obj.PainterName in adict:
                adict[obj.PainterName]+=1
            else:
                adict[obj.PainterName]=1
        res=sorted(adict.items(),key=lambda item:item[1],reverse=True)     
        return res

if __name__=="__main__":
    n=int(input())
    alist=[]
    for i in range(n):
        ids=int(input()) 
        name=input()
        price=int(input())
        type1=input()
        alist.append(Painting(ids,name,price,type1))                      
    string=input()
    obj=ShowRoom(alist)
    o1=obj.getTotalPaintingPrice(string)[0]
    print(o1)
    o2=obj.getPainterkithaxCountOfPaintings()[0][0]
    print(o2)