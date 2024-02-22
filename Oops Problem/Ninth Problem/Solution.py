class Book:
    def __init__(self,BookId,BookName,AuthorName):
        self.BookId=BookId
        self.BookName=BookName
        self.AuthorName=AuthorName


class Library:
    def __init__(self,BookList,LibAddress):
        self.BookList=BookList
        self.LibAddress=LibAddress

    def CountEachAuthorBook(self):
        adict={}
        for obj in self.BookList:
            key=obj.AuthorName.upper()

            if key in adict:
                adict[key]+=1
            else:
                adict[key]=1  
        return adict          
                    

# def function(city,BookList):
#     alist=[]
#     for item in BookList:
#         for _,v in item.items():
#             if v==city:
#                 alist.append(item)
#     return alist

if __name__=="__main__":
    LibraryObjList=[]
    BookList=[]
    LibAddress={}
    n=int(input())
    for i in range(n):
        for j in range(int(input())):
            bookid=int(input())
            bookname=input().lower()
            authorname=input().lower()
            BookList.append(Book(bookid,bookname,authorname))
        address={'street':0,'area':0,'city':0,'state':0,'zip':0}
        for k,v in address.items():
            address[k]=input()
        LibraryObjList.append(Library(BookList,LibAddress))    

    city = input()
    obj=Library(BookList,LibAddress)
    # for j in range(n):
    #     obj = LibraryObjList[j]
    res=obj.CountEachAuthorBook()
    # res = obj.booksByAuthors()
    for k,v in res.items():
        print(k,v)
    # print(*res.keys(), *res.values())
    # books = findbookType(city,libObj)
    # print(books)



     




            



